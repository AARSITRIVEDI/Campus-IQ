import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import textwrap

output_pdf = "Campus_IQ_Midterm_Evaluation_Defense_Guide.pdf"

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

def create_page():
    fig, ax = plt.subplots(figsize=(8.27, 11.69), dpi=150) # A4 size
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    return fig, ax

def add_header(ax, title, subtitle):
    # Header bar
    ax.fill_between([5, 95], [92, 92], [97, 97], color='#1e3a8a')
    ax.text(50, 94.5, title.upper(), color='white', fontsize=12, fontweight='bold', ha='center', va='center')
    ax.text(50, 90.0, subtitle, color='#475569', fontsize=9, fontstyle='italic', ha='center', va='center')
    ax.plot([5, 95], [88, 88], color='#cbd5e1', lw=1)

def add_footer(ax, page_num, total_pages=5):
    ax.plot([5, 95], [6, 6], color='#cbd5e1', lw=1)
    ax.text(5, 4.2, "Campus IQ — CSET-211 Statistical Machine Learning Mid-Term Evaluation", color='#64748b', fontsize=7.5, va='center')
    ax.text(95, 4.2, f"Page {page_num} of {total_pages}", color='#64748b', fontsize=7.5, ha='right', va='center')

with PdfPages(output_pdf) as pdf:
    # ---------------- PAGE 1: TITLE & QUESTION 1 (PROBLEM STATEMENT) ----------------
    fig, ax = create_page()
    add_header(ax, "Campus IQ: Mid-Term Evaluation Defense Guide", "Course: CSET-211 Statistical Machine Learning | Milestone 2 Scope: 50.0% Completed")
    
    # Metadata Box
    ax.fill_between([5, 95], [77, 77], [86.5, 86.5], color='#f8fafc')
    ax.plot([5, 95, 95, 5, 5], [77, 77, 86.5, 86.5, 77], color='#cbd5e1', lw=1)
    ax.text(7, 84, "TEAM MEMBERS:", color='#1e3a8a', fontsize=8.5, fontweight='bold')
    ax.text(7, 81.5, "• AARSI TRIVEDI (S25CSEU1882) - Project Lead\n• ARJU (S25CSEU1868) | ANGEL (S25CSEU1873)", color='#1e293b', fontsize=8)
    ax.text(55, 84, "MILESTONE STATUS & SCOPE:", color='#1e3a8a', fontsize=8.5, fontweight='bold')
    ax.text(55, 81.5, "• Current Progress: 50.0% (Phase 1 Complete)\n• Focus: Sports Complex, Hypothesis Testing, EDA", color='#166534', fontsize=8)

    # Q1: Problem Statement
    ax.fill_between([5, 95], [71.5, 71.5], [75, 75], color='#e2e8f0')
    ax.text(7, 73.2, "1. PROBLEM STATEMENT", color='#0f172a', fontsize=10, fontweight='bold', va='center')

    q1_text = (
        "University campuses operate under bursty, uncoordinated, and synchronized schedules. Unlike commercial "
        "facilities with advance bookings, campus amenities operate as open-access commons, causing acute and "
        "predictable bottlenecks:\n\n"
        "1. Sports Complex Overcrowding (Primary Milestone 2 Target): Peak evening hours (17:00–20:00) and weekends "
        "see attendance surging up to 130 visitors against a 200 physical capacity (load > 80% to 108% in concentrated "
        "gym and badminton areas), causing equipment shortages, safety risks, and wasted student transit trips.\n\n"
        "2. Cafeteria Volatility & Food Waste (SDG 12 Target 12.3): Lunch demand (12:00–14:00) jumps to 141.3 orders "
        "vs 67.8 off-peak. Lack of forward forecasts forces kitchens into guesswork batch cooking, resulting in preventable "
        "food surplus spoilage or sudden stockouts.\n\n"
        "3. Library Study Bottlenecks (SDG 11 Target 11.7): Study occupancy explodes by +260% during midterms and exams "
        "(jumping from 43.5 to 156.8 seats), creating severe seat shortages and study displacement."
    )
    wrapped_q1 = textwrap.fill(q1_text, width=88)
    ax.text(7, 69.5, wrapped_q1, color='#1e293b', fontsize=8.2, va='top', linespacing=1.35)

    # Root Cause Box
    ax.fill_between([5, 95], [17, 17], [30, 30], color='#eff6ff')
    ax.plot([5, 95, 95, 5, 5], [17, 17, 30, 30, 17], color='#93c5fd', lw=1)
    ax.text(7, 28, "ROOT CAUSE ANALYSIS:", color='#1d4ed8', fontsize=8.5, fontweight='bold')
    root_text = (
        "• Timetable Synchronization: When lectures in academic blocks conclude simultaneously (classes_ending_nearby), "
        "hundreds of students flood adjacent facilities within 15–30 minutes.\n"
        "• Purely Reactive Awareness: Students and staff only discover overcrowding after physically reaching the venue.\n"
        "• Siloed Operations: Gym staff, kitchen managers, and librarians do not share data, failing to anticipate spillover waves."
    )
    ax.text(7, 26, root_text, color='#1e293b', fontsize=8, va='top', linespacing=1.35)

    # Q2: Solution
    ax.fill_between([5, 95], [9.5, 9.5], [13, 13], color='#e2e8f0')
    ax.text(7, 11.2, "2. SOLUTION OF THE PROBLEM STATEMENT (CAMPUS DEMAND FLOW)", color='#0f172a', fontsize=10, fontweight='bold', va='center')
    sol_summary = "Campus IQ replaces reactive counting with proactive, interpretable classical SML forecasting 2-4 hours ahead."
    ax.text(7, 8.2, sol_summary, color='#1e293b', fontsize=8, va='top')

    add_footer(ax, 1)
    pdf.savefig(fig)
    plt.close()

    # ---------------- PAGE 2: QUESTION 2 CONTINUED & QUESTION 3 (FEATURES) ----------------
    fig, ax = create_page()
    add_header(ax, "Campus IQ: Mid-Term Evaluation Defense Guide", "Section 2: Solution Pillars & Section 3: Key Features (50% Milestone Demarcation)")

    # Solution Pillars
    sol_pillars = (
        "Campus IQ models campus dynamics through the 'Campus Demand Flow' framework:\n"
        "Activity (Timetable/Events)  -->  Facility Demand  -->  Congestion Risk (>=80%)  -->  Prescriptive Load Shifting\n\n"
        "• Proactive Forecasting: Predicts visitor volumes 2-4 hours ahead, eliminating wasted student transit.\n"
        "• Interpretable Classical SML: Strictly classical algorithms (Linear Regression, Ridge, Random Forest, Logistic Regression) "
        "with complete feature attribution (Gini importance, coefficients). Zero black-box neural networks or LLMs.\n"
        "• Interconnected Flow Dynamics: Captures human spillovers: Lecture --> Sports Complex --> Cafeteria --> Library.\n"
        "• Prescriptive Load Shifting: Suggests concrete alternative time slots with crowd reduction metrics (-48.5% crowd).\n"
        "• Calibrated Kitchen Preparation: Formulates demand distributions for kitchens to prepare food within +-5% safety margins."
    )
    ax.text(7, 85, sol_pillars, color='#1e293b', fontsize=8.2, va='top', linespacing=1.35)

    # Q3: Key Features
    ax.fill_between([5, 95], [59, 59], [62.5, 62.5], color='#e2e8f0')
    ax.text(7, 60.7, "3. KEY FEATURES: 50% COMPLETED (PHASE 1) VS 50% PLANNED (PHASE 2)", color='#0f172a', fontsize=10, fontweight='bold', va='center')

    # Features Table
    table_data = [
        ["Phase", "Feature Name", "Technical Implementation", "Status"],
        ["Phase 1\n(50% Mid)", "Sports Demand Regression", "Linear Reg (R2=0.4061) vs Random Forest (R2=0.8839, MAE=6.60 visitors)", "COMPLETED"],
        ["Phase 1\n(50% Mid)", "Overcrowding Risk Classifier", "Logistic Reg (85.7% acc) vs Random Forest (91.8% acc, 88.9% recall)", "COMPLETED"],
        ["Phase 1\n(50% Mid)", "Campus Pulse Index (CPI)", "Normalized composite 0-100 metric: 0.35*Sports + 0.30*Lib + 0.25*Food + 0.10*Workload", "COMPLETED"],
        ["Phase 1\n(50% Mid)", "Statistical Rigor & Demo UI", "Welch's t-test, Mann-Whitney U, 1.5x IQR outlier retention; live demo web UI", "COMPLETED"],
        ["Phase 2\n(50% Final)", "Food Outlets ML Engine", "Ridge & Gradient Boosting predicting exact meal orders and surplus/shortage for SDG 12", "PLANNED (M3)"],
        ["Phase 2\n(50% Final)", "Library Study Space ML", "Poisson / Random Forest predicting exam crunch study hall occupancy for SDG 11", "PLANNED (M3)"],
        ["Phase 2\n(50% Final)", "K-Means Clustering & PCA", "Unsupervised clustering (K=3) & 2D PCA projecting student activity personas", "PLANNED (M3)"],
        ["Phase 2\n(50% Final)", "Production Web Dashboard", "Real-time CPI gauge, live recommendation carousel, and interactive simulator", "PLANNED (M3)"],
    ]

    col_widths = [15, 23, 42, 10]
    y_start = 57
    row_height = 4.8
    for row_idx, row in enumerate(table_data):
        y = y_start - (row_idx * row_height)
        bg_col = '#1e3a8a' if row_idx == 0 else ('#f1f5f9' if row_idx % 2 == 1 else '#ffffff')
        ax.fill_between([5, 95], [y - 4.2, y - 4.2], [y, y], color=bg_col)
        ax.plot([5, 95, 95, 5, 5], [y - 4.2, y - 4.2, y, y, y - 4.2], color='#cbd5e1', lw=0.5)
        
        cur_x = 7
        for c_idx, val in enumerate(row):
            txt_col = '#ffffff' if row_idx == 0 else ('#166534' if val == 'COMPLETED' else ('#1e293b' if val != 'PLANNED (M3)' else '#1e40af'))
            font_wt = 'bold' if (row_idx == 0 or c_idx == 3 or c_idx == 1) else 'normal'
            ax.text(cur_x, y - 2.5, val, color=txt_col, fontsize=7.2, fontweight=font_wt, va='center')
            cur_x += col_widths[c_idx]

    add_footer(ax, 2)
    pdf.savefig(fig)
    plt.close()

    # ---------------- PAGE 3: QUESTION 4 (GOALS) & QUESTION 5 (EXISTING VS CAMPUS IQ) ----------------
    fig, ax = create_page()
    add_header(ax, "Campus IQ: Mid-Term Evaluation Defense Guide", "Section 4: Project Goals & UN-SDGs | Section 5: Comparative Analysis")

    # Q4: Goals
    ax.fill_between([5, 95], [83.5, 83.5], [87, 87], color='#e2e8f0')
    ax.text(7, 85.2, "4. PROJECT GOALS & UN SUSTAINABLE DEVELOPMENT GOALS (SDGS)", color='#0f172a', fontsize=10, fontweight='bold', va='center')

    goals_text = (
        "• Academic Goals: Rigorous classical SML curriculum compliance (CSET-211), parametric vs non-parametric testing, "
        "zero lookahead data leakage via strict chronological 80/20 train/test splitting, and full Gini interpretability.\n"
        "• Operational Goals: Flatten peak congestion curves, prevent equipment bottlenecks, and eliminate wasted student transit.\n\n"
        "UN-SDG 11: Sustainable Cities & Communities (Target 11.7 - Safe and Inclusive Public Spaces)\n"
        "Campuses act as mini-cities. Campus IQ ensures safe, equitable access to sports and study infrastructure by detecting "
        "overcrowding (>=80%) hours in advance, preserving physical safety, and eliminating seat/equipment hoarding.\n\n"
        "UN-SDG 12: Responsible Consumption & Production (Target 12.3 - Halve Food Waste)\n"
        "Campus dining halls produce avoidable waste from rigid batch cooking. Campus IQ formulates exact food balance equations: "
        "Surplus = max(0, Prep - Sold); Shortage = max(0, Demand - Prep). Forecasting meal demand enables batching within +-5%."
    )
    ax.text(7, 81.5, goals_text, color='#1e293b', fontsize=8.2, va='top', linespacing=1.35)

    # Q5: Comparative Analysis
    ax.fill_between([5, 95], [51.5, 51.5], [55, 55], color='#e2e8f0')
    ax.text(7, 53.2, "5. DIFFERENCE BETWEEN EXISTING SOLUTIONS AND CAMPUS IQ", color='#0f172a', fontsize=10, fontweight='bold', va='center')

    comp_table = [
        ["Dimension", "Google Maps 'Popular Times'", "Turnstiles / IoT Cameras", "Campus IQ (Our System)"],
        ["Paradigm", "Historical aggregates", "Strictly Reactive (counts now)", "Proactive Predictive (2-4 hrs ahead)"],
        ["Hardware Cost", "High (requires cell telemetry)", "Very High (sensors, gates, wiring)", "Zero Added Cost (uses campus logs)"],
        ["Campus Context", "Blind to exams and timetables", "Blind to reasons; doorway only", "Deeply Integrated (exams, classes, events)"],
        ["Facility Scope", "Siloed individual map pins", "Siloed single entry points", "Interconnected Demand Flow Network"],
        ["Interpretability", "Proprietary black-box", "Hardware count logic", "100% Explainable Classical ML"],
        ["Actionability", "Visual bar chart only", "Red/Green light at gate", "Alternative time slots with Delta % relief"],
        ["Sustainability", "None", "None", "Direct SDG 11 & SDG 12 Formulations"],
    ]

    col_widths_c = [16, 26, 26, 24]
    y_start_c = 49.5
    row_height_c = 4.8
    for row_idx, row in enumerate(comp_table):
        y = y_start_c - (row_idx * row_height_c)
        bg_col = '#1e3a8a' if row_idx == 0 else ('#f1f5f9' if row_idx % 2 == 1 else '#ffffff')
        ax.fill_between([5, 95], [y - 4.2, y - 4.2], [y, y], color=bg_col)
        ax.plot([5, 95, 95, 5, 5], [y - 4.2, y - 4.2, y, y, y - 4.2], color='#cbd5e1', lw=0.5)
        
        cur_x = 7
        for c_idx, val in enumerate(row):
            txt_col = '#ffffff' if row_idx == 0 else ('#166534' if c_idx == 3 and row_idx > 0 else '#1e293b')
            font_wt = 'bold' if (row_idx == 0 or c_idx == 3 or c_idx == 0) else 'normal'
            ax.text(cur_x, y - 2.5, val, color=txt_col, fontsize=7.2, fontweight=font_wt, va='center')
            cur_x += col_widths_c[c_idx]

    add_footer(ax, 3)
    pdf.savefig(fig)
    plt.close()

    # ---------------- PAGE 4: QUESTION 6 (TECHNICAL IMPLEMENTATION: DATA & STATS) ----------------
    fig, ax = create_page()
    add_header(ax, "Campus IQ: Mid-Term Evaluation Defense Guide", "Section 6.1: Data Pipeline, Preprocessing & Section 6.2: Statistical Rigor")

    # Q6: Technical Implementation Part 1
    ax.fill_between([5, 95], [83.5, 83.5], [87, 87], color='#e2e8f0')
    ax.text(7, 85.2, "6. TECHNICAL IMPLEMENTATION: DATASET, PREPROCESSING & STATISTICAL RIGOR", color='#0f172a', fontsize=10, fontweight='bold', va='center')

    tech_p1 = (
        "• Dataset Ingestion: 490 longitudinal records (data/user_uploaded_campus_data.csv) spanning Aug 3 - Oct 11, 2026.\n"
        "• Data Preprocessing: 450 null entries in event_type matched non-event days (campus_event_flag == 0); systematically "
        "imputed with 'None'. Extracted starting_hour, day_of_week_num, and is_weekend flags.\n"
        "• Zero Lookahead Data Leakage: Strict chronological 80/20 train/test split (Train: 392 rows | Test: 98 rows).\n"
        "• Outlier Analysis (1.5x IQR Rule): Upper fence for sports visitors = Q3 + 1.5*IQR = 83.0 + 1.5(58.0) = 170.0 visitors. "
        "Max observed visitors = 130 (108.3% capacity in gym/courts). All observations retained because real-world surge "
        "events (tournaments) represent legitimate high-impact operational events that the ML system must anticipate."
    )
    ax.text(7, 81.5, tech_p1, color='#1e293b', fontsize=8.2, va='top', linespacing=1.35)

    # Hypothesis Testing Box
    ax.fill_between([5, 95], [26, 26], [58, 58], color='#0f172a')
    ax.text(7, 55.5, "FORMAL STATISTICAL HYPOTHESIS TESTING (alpha = 0.05):", color='#38bdf8', fontsize=8.5, fontweight='bold')
    
    ht_text = (
        "TEST 1: Sports Complex Weekend vs. Weekday Demand\n"
        "• Weekend (n=140): Mean = 60.3 visitors (std = 33.2)  |  Weekday (n=350): Mean = 47.6 visitors (std = 29.5)\n"
        "• Welch's t-test: t = 4.1967 (p = 3.71e-05)  |  Mann-Whitney U: U = 31798.0 (p = 2.54e-07)  |  Cohen's d: 0.4145\n"
        "• Decision: REJECT NULL HYPOTHESIS (p < 0.001). Weekend demand is significantly higher than weekday demand.\n\n"
        "TEST 2: Library Study Space Occupancy: Midterms vs. Regular Semester\n"
        "• Midterm (n=56): Mean = 156.8 seats (std = 18.2)  |  Regular (n=434): Mean = 43.5 seats (std = 20.8)\n"
        "• Welch's t-test: t = 41.1962 (p = 5.31e-51)  |  Mann-Whitney U: U = 24304.0 (p = 3.64e-34)  |  Cohen's d: 5.7911\n"
        "• Decision: REJECT NULL HYPOTHESIS (p < 0.001). Library demand surges by +260% during midterms.\n\n"
        "TEST 3: Cafeteria Lunch Rush (12:00-14:00) Concentration (SDG 12 Food Waste Risk)\n"
        "• Lunch Rush (n=70): Mean = 141.3 orders (std = 28.5)  |  Off-Peak (n=420): Mean = 67.8 orders (std = 34.7)\n"
        "• Welch's t-test: t = 27.5346 (p = 7.33e-67)  |  Mann-Whitney U: U = 28421.5 (p = 6.48e-36)  |  Cohen's d: 2.2275\n"
        "• Decision: REJECT NULL HYPOTHESIS (p < 0.001). Meal demand is severely concentrated, confirming shortage risk."
    )
    ax.text(7, 53, ht_text, color='#f8fafc', fontsize=7.6, fontfamily='monospace', va='top', linespacing=1.25)

    # Feature Engineering
    ax.fill_between([5, 95], [8, 8], [24, 24], color='#f8fafc')
    ax.plot([5, 95, 95, 5, 5], [8, 8, 24, 24, 8], color='#cbd5e1', lw=1)
    ax.text(7, 22, "DOMAIN FEATURE ENGINEERING & CPI FORMULATION:", color='#1e3a8a', fontsize=8.5, fontweight='bold')
    fe_text = (
        "• Sports Load (%) = (Sports Visitors / 200) * 100  |  Overcrowded Flag = 1 if Sports Load >= 80.0% else 0\n"
        "• Kitchen Balance: Food Sold = min(Prep, Demand) | Surplus = max(0, Prep - Sold) | Shortage = max(0, Demand - Prep)\n"
        "• Campus Pulse Index (CPI): CPI = 0.35*SportsLoad + 0.30*LibraryLoad + 0.25*FoodNorm + 0.10*WorkloadScore\n"
        "  Rationale: Sports (0.35) is tightest physical bottleneck; Library (0.30) captures academic volume; Cafeteria (0.25) "
        "reflects waste; Workload (0.10) is behavioral driver. Weights sum exactly to 1.00."
    )
    ax.text(7, 19.5, fe_text, color='#1e293b', fontsize=7.8, va='top', linespacing=1.35)

    add_footer(ax, 4)
    pdf.savefig(fig)
    plt.close()

    # ---------------- PAGE 5: QUESTION 6 CONTINUED (ML BENCHMARKS) & VIVA Q&A ----------------
    fig, ax = create_page()
    add_header(ax, "Campus IQ: Mid-Term Evaluation Defense Guide", "Section 6.3: ML Benchmarks & Section 7: Teacher Viva Defense Cheat Sheet")

    # ML Benchmarks Table
    ax.fill_between([5, 95], [83.5, 83.5], [87, 87], color='#e2e8f0')
    ax.text(7, 85.2, "6.3 BASELINE MACHINE LEARNING BENCHMARKS (SPORTS COMPLEX TARGET)", color='#0f172a', fontsize=10, fontweight='bold', va='center')

    ml_table = [
        ["Task & Target", "Model Candidate", "Metric 1", "Metric 2", "Operational Evaluation"],
        ["Continuous Regression\n(Sports Visitors)", "Linear Regression", "MAE = 19.96", "R2 = 0.4061", "Baseline linear fit; misses non-linear evening spikes."],
        ["Continuous Regression\n(Sports Visitors)", "Random Forest Regressor", "MAE = 6.60", "R2 = 0.8839", "SELECTED BEST: Strong non-linear interactions (RMSE=10.30)."],
        ["Binary Classification\n(>= 80% Overcrowding)", "Logistic Regression", "Accuracy = 85.7%", "Recall = 55.6%", "Baseline linear boundary; misses 44.4% of critical events."],
        ["Binary Classification\n(>= 80% Overcrowding)", "Random Forest Classifier", "Accuracy = 91.8%", "Recall = 88.9%", "SELECTED BEST: Catches 8 of 9 critical events (F1=0.6667)."],
    ]

    col_widths_m = [20, 22, 16, 16, 20]
    y_start_m = 81.5
    row_height_m = 5.2
    for row_idx, row in enumerate(ml_table):
        y = y_start_m - (row_idx * row_height_m)
        bg_col = '#1e3a8a' if row_idx == 0 else ('#f1f5f9' if row_idx % 2 == 1 else '#ffffff')
        ax.fill_between([5, 95], [y - 4.6, y - 4.6], [y, y], color=bg_col)
        ax.plot([5, 95, 95, 5, 5], [y - 4.6, y - 4.6, y, y, y - 4.6], color='#cbd5e1', lw=0.5)
        
        cur_x = 7
        for c_idx, val in enumerate(row):
            txt_col = '#ffffff' if row_idx == 0 else ('#166534' if 'SELECTED BEST' in val else '#1e293b')
            font_wt = 'bold' if (row_idx == 0 or 'SELECTED BEST' in val or c_idx == 1) else 'normal'
            ax.text(cur_x, y - 2.5, val, color=txt_col, fontsize=7.1, fontweight=font_wt, va='center')
            cur_x += col_widths_m[c_idx]

    # Confusion Matrix & Gini Importance
    ax.fill_between([5, 48], [42, 42], [54, 54], color='#eff6ff')
    ax.plot([5, 48, 48, 5, 5], [42, 42, 54, 54, 42], color='#93c5fd', lw=1)
    ax.text(7, 52.2, "CONFUSION MATRIX (Test N=98):", color='#1d4ed8', fontsize=8, fontweight='bold')
    cm_text = "TN = 82  |  FP = 7\nFN = 1   |  TP = 8\nRecall = 88.9% (8/9 caught)\nPrecision = 53.3% | Acc = 91.8%"
    ax.text(7, 50, cm_text, color='#1e293b', fontsize=7.8, va='top', fontfamily='monospace', linespacing=1.2)

    ax.fill_between([52, 95], [42, 42], [54, 54], color='#f0fdf4')
    ax.plot([52, 95, 95, 52, 52], [42, 42, 54, 54, 42], color='#86efac', lw=1)
    ax.text(54, 52.2, "GINI FEATURE IMPORTANCE:", color='#166534', fontsize=8, fontweight='bold')
    gini_text = "1. starting_hour: 79.20%\n2. is_midterm: 4.63%\n3. academic_workload: 4.58%\n4. campus_event_flag: 4.22%"
    ax.text(54, 50, gini_text, color='#1e293b', fontsize=7.8, va='top', fontfamily='monospace', linespacing=1.2)

    # Viva Defense Q&A Cheat Sheet
    ax.fill_between([5, 95], [36.5, 36.5], [40, 40], color='#e2e8f0')
    ax.text(7, 38.2, "7. TOP EXAMINER VIVA QUESTIONS & RECOMMENDED DEFENSE", color='#0f172a', fontsize=10, fontweight='bold', va='center')

    viva_text = (
        "Q1: Why is the project at 50% right now? Is this adequate?\n"
        "A (Aarsi): Yes. The official course rubric for Milestone 2 specifies a 30% to 50% scope. We have completed exactly "
        "50.0% (Phase 1): data ingestion, temporal preprocessing, hypothesis testing, and benchmarked models for the primary "
        "target (Sports Complex). The remaining 50% (Phase 2) is scheduled for Milestone 3 (Food/Library models, K-Means, Dashboard).\n\n"
        "Q2: Why not use deep neural networks (LSTMs or Transformers)?\n"
        "A (Angel): This is CSET-211: Statistical Machine Learning, which mandates interpretable models. On tabular time-series "
        "with 490 rows, deep learning overfits heavily, whereas Random Forest achieves R2=0.8839 and MAE=6.6 with full Gini attribution.\n\n"
        "Q3: How did you prevent data leakage in your time-series data?\n"
        "A (Arju): Random cross-validation leaks future information. We strictly partitioned the 490 rows chronologically (80% train / "
        "20% test). The test set (final 98 rows) was held out untouched until final model evaluation."
    )
    ax.text(7, 34.5, viva_text, color='#1e293b', fontsize=7.8, va='top', linespacing=1.28)

    add_footer(ax, 5)
    pdf.savefig(fig)
    plt.close()

print(f"Successfully generated {output_pdf} (size: {os.path.getsize(output_pdf)} bytes)")
