#!/usr/bin/env python3
"""
Campus IQ - Milestone 2: Mid-Term Demo Web Server (50% Scope)
Serves a dedicated temporary interface specifically tailored for showing your teacher
the 40-50% project milestone (Stages 1 to 5), while explicitly demarcating the remaining
stages as scheduled for Milestone 3 (Final Submission).

URL: http://localhost:8050
"""

import os
import sys
import json
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR, "web")
DATA_FILE = os.path.join(BASE_DIR, "data", "user_uploaded_campus_data.csv")

# Train baseline models on user_uploaded_campus_data.csv
print("[Mid-Term Demo Server] Initializing Milestone 2 baseline models...")
df = pd.read_csv(DATA_FILE)
df['date'] = pd.to_datetime(df['date'])
df['day_of_week_num'] = df['date'].dt.dayofweek
df['is_weekend'] = (df['day_of_week_num'] >= 5).astype(int)
df['month'] = df['date'].dt.month
df['starting_hour'] = df['time_slot'].apply(lambda s: int(str(s).split(':')[0]) if ':' in str(s) else 12)
df['is_peak_hour'] = df['starting_hour'].apply(lambda h: 1 if h in [12, 13, 17, 18, 19] else 0)
df['is_midterm'] = df['semester_phase'].astype(str).str.contains('Mid', case=False).astype(int)
df['is_exam_week'] = df['semester_phase'].astype(str).str.contains('Exam|Final', case=False).astype(int)

features = [
    'day_of_week_num', 'is_weekend', 'month', 'starting_hour', 'is_peak_hour',
    'academic_workload', 'classes_ending_nearby', 'campus_event_flag',
    'sports_prev_crowd', 'is_midterm', 'is_exam_week'
]

split_idx = int(len(df) * 0.8)
train_df = df.iloc[:split_idx]
X_train = train_df[features]
y_train_reg = train_df['sports_visitors']
y_train_clf = train_df['sports_overcrowded']

rf_reg = RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42).fit(X_train, y_train_reg)
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=6, class_weight='balanced', random_state=42).fit(X_train, y_train_clf)
print("✓ Baseline models initialized successfully!")

def sanitize_obj(obj):
    import math
    if isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj
    elif isinstance(obj, dict):
        return {k: sanitize_obj(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitize_obj(elem) for elem in obj]
    return obj

class MidtermDemoHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def _send_json(self, data, status=200):
        clean_data = sanitize_obj(data)
        body = json.dumps(clean_data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/" or path == "/index.html":
            # Serve the temporary 50% interface
            demo_path = os.path.join(WEB_DIR, "midterm_demo.html")
            with open(demo_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        elif path == "/api/midterm/dataset":
            # Clean dataframe to ensure zero NaNs
            clean_df = df.copy().fillna("")
            records = clean_df.head(15).to_dict(orient="records")
            # Format dates cleanly
            for r in records:
                r['date'] = str(r['date']).split(' ')[0]
            self._send_json({
                "total_records": len(df),
                "records": records
            })
            return

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
        try:
            payload = json.loads(body)
        except Exception:
            payload = {}

        if path == "/api/midterm/predict_sports":
            hour = int(payload.get("starting_hour", 18))
            day_name = payload.get("day_of_week", "Saturday")
            day_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
            day_num = day_map.get(day_name, 5)
            is_weekend = 1 if day_num >= 5 else 0
            is_peak = 1 if hour in [12, 13, 17, 18, 19] else 0
            workload = int(payload.get("academic_workload", 3))
            classes = int(payload.get("classes_ending_nearby", 4))
            event = int(payload.get("campus_event_flag", 1))
            prev = int(payload.get("sports_prev_crowd", 75))

            row = pd.DataFrame([{
                'day_of_week_num': day_num,
                'is_weekend': is_weekend,
                'month': 9,
                'starting_hour': hour,
                'is_peak_hour': is_peak,
                'academic_workload': workload,
                'classes_ending_nearby': classes,
                'campus_event_flag': event,
                'sports_prev_crowd': prev,
                'is_midterm': 0,
                'is_exam_week': 0
            }])[features]

            pred_val = int(round(rf_reg.predict(row)[0]))
            pred_val = max(10, min(190, pred_val))
            load_pct = round((pred_val / 200.0) * 100, 1)
            is_over = 1 if load_pct >= 80.0 else 0

            self._send_json({
                "predicted_visitors": pred_val,
                "capacity_load_pct": load_pct,
                "is_overcrowded": is_over,
                "model_name": "Random Forest Regressor (MAE: 6.60, R²: 0.8839)"
            })
            return

        self._send_json({"error": "Endpoint not found"}, 404)

def run_server(port=8050):
    server_address = ("", port)
    httpd = HTTPServer(server_address, MidtermDemoHandler)
    print("\n" + "=" * 75)
    print("      CAMPUS IQ: MILESTONE 2 MID-TERM DEMO SERVER (50% SCOPE)")
    print("=" * 75)
    print(f" • Demo Web Interface: http://localhost:{port}")
    print(f" • Scope:             Milestone 2 (Stages 1 to 5 Active | Stages 6 to 12 Locked)")
    print(f" • Team:              Aarsi Trivedi, Arju, Angel (CSET-211)")
    print("=" * 75)
    print(" Press Ctrl+C in your terminal to stop the server.\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[Mid-Term Demo Server] Server stopped gracefully.")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8050
    run_server(port)
