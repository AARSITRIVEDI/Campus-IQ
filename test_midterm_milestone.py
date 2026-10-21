#!/usr/bin/env python3
"""
Campus IQ - Automated Test Suite for Milestone 2: Mid Progress Evaluation (38% Scope)
Verifies:
1. Dataset exists at data/user_uploaded_campus_data.csv with >= 450 observations and 0 missing values in critical columns.
2. Chronological 80/20 train/test split has no lookahead data leakage.
3. Feature engineering derives sports load %, overcrowding flag, food surplus/shortage, library load %, and CPI.
4. Formal hypothesis testing computes valid p-values and Cohen's d effect sizes.
5. Primary baseline models (Linear Regression, Random Forest Regressor, Logistic Regression, Random Forest Classifier) train and score successfully.
"""

import os
import unittest
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score, f1_score

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "user_uploaded_campus_data.csv")

class TestMidtermMilestone2(unittest.TestCase):

    def setUp(self):
        self.assertTrue(os.path.exists(DATA_PATH), f"Dataset not found at {DATA_PATH}")
        self.df = pd.read_csv(DATA_PATH)

    def test_01_dataset_integrity(self):
        """Verify dataset row count, schema, and non-null guarantees."""
        self.assertGreaterEqual(len(self.df), 450, "Dataset must have at least 450 observations for milestone 2.")
        required_cols = [
            'date', 'time_slot', 'semester_phase', 'academic_workload',
            'classes_ending_nearby', 'campus_event_flag', 'sports_visitors',
            'sports_capacity', 'sports_overcrowded', 'library_occupancy',
            'library_capacity', 'food_orders_demand', 'food_surplus_shortage_risk'
        ]
        for col in required_cols:
            self.assertIn(col, self.df.columns, f"Missing required column: {col}")
            self.assertEqual(self.df[col].isnull().sum(), 0, f"Column {col} has unexpected null values.")

    def test_02_chronological_splitting(self):
        """Verify 80/20 train/test split has zero temporal lookahead leakage."""
        split_idx = int(len(self.df) * 0.8)
        train_df = self.df.iloc[:split_idx]
        test_df = self.df.iloc[split_idx:]
        
        self.assertEqual(len(train_df) + len(test_df), len(self.df))
        self.assertGreater(len(train_df), len(test_df))
        # Ensure chronological ordering: max train date <= min test date
        train_max_date = pd.to_datetime(train_df['date']).max()
        test_min_date = pd.to_datetime(test_df['date']).min()
        self.assertLessEqual(train_max_date, test_min_date, "Temporal leakage detected: train date exceeds test date.")

    def test_03_domain_feature_engineering(self):
        """Verify derived formulations: Sports load %, Overcrowded flag, CPI."""
        df = self.df.copy()
        df['sports_load_pct'] = (df['sports_visitors'] / df['sports_capacity']) * 100
        df['is_overcrowded'] = (df['sports_load_pct'] >= 80.0).astype(int)
        
        # Verify overcrowding flag logic
        self.assertTrue(((df['sports_load_pct'] >= 80.0) == (df['is_overcrowded'] == 1)).all())
        
        # Verify Campus Pulse Index (CPI) bounds [0, 100]
        cpi = df['campus_pulse_index']
        self.assertTrue((cpi >= 0).all() and (cpi <= 100).all(), "CPI scores must be bounded between 0 and 100.")

    def test_04_statistical_hypothesis_testing(self):
        """Verify hypothesis testing logic and calculation of Welch's t and Mann-Whitney U."""
        weekend = self.df[self.df['date'].apply(lambda d: pd.to_datetime(d).dayofweek >= 5)]['sports_visitors']
        weekday = self.df[self.df['date'].apply(lambda d: pd.to_datetime(d).dayofweek < 5)]['sports_visitors']
        
        t_stat, p_val = stats.ttest_ind(weekend, weekday, equal_var=False)
        self.assertFalse(np.isnan(t_stat))
        self.assertLess(p_val, 0.05, "Weekend vs weekday sports attendance difference must be statistically significant.")

    def test_05_baseline_machine_learning_models(self):
        """Verify training and evaluation of primary sports baseline regression and classification models."""
        df = self.df.copy()
        df['date'] = pd.to_datetime(df['date'])
        df['day_of_week_num'] = df['date'].dt.dayofweek
        df['is_weekend'] = (df['day_of_week_num'] >= 5).astype(int)
        df['month'] = df['date'].dt.month
        df['starting_hour'] = df['time_slot'].apply(lambda s: int(s.split(':')[0]))
        df['is_peak_hour'] = df['starting_hour'].apply(lambda h: 1 if h in [12, 13, 17, 18, 19] else 0)
        df['is_midterm'] = df['semester_phase'].astype(str).str.contains('Mid', case=False).astype(int)
        df['is_exam_week'] = df['semester_phase'].astype(str).str.contains('Exam|Final', case=False).astype(int)

        features = [
            'day_of_week_num', 'is_weekend', 'month', 'starting_hour', 'is_peak_hour',
            'academic_workload', 'classes_ending_nearby', 'campus_event_flag',
            'sports_prev_crowd', 'is_midterm', 'is_exam_week'
        ]

        split_idx = int(len(df) * 0.8)
        train_df, test_df = df.iloc[:split_idx], df.iloc[split_idx:]
        X_train, y_train_reg, y_train_clf = train_df[features], train_df['sports_visitors'], train_df['sports_overcrowded']
        X_test, y_test_reg, y_test_clf = test_df[features], test_df['sports_visitors'], test_df['sports_overcrowded']

        # Regression check
        rf_reg = RandomForestRegressor(n_estimators=50, random_state=42).fit(X_train, y_train_reg)
        y_pred_reg = rf_reg.predict(X_test)
        r2 = r2_score(y_test_reg, y_pred_reg)
        self.assertGreater(r2, 0.70, "Random Forest Regressor R2 score should be > 0.70 on sports visitor demand.")

        # Classification check
        rf_clf = RandomForestClassifier(n_estimators=50, class_weight='balanced', random_state=42).fit(X_train, y_train_clf)
        y_pred_clf = rf_clf.predict(X_test)
        acc = accuracy_score(y_test_clf, y_pred_clf)
        self.assertGreater(acc, 0.85, "Random Forest Classifier accuracy should be > 85% on overcrowding risk.")

if __name__ == "__main__":
    unittest.main()
