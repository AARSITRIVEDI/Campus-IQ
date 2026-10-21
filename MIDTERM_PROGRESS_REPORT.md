# Project Milestone 2: Statistical Machine Learning (CSET-211)
## Mid Progress Report: Campus IQ (38.5% Completion Scope)

> **Submission Form Reference:** `Project_Milestone 2_Statistical Machine Learning(CSET-211)-Mid Progress Report`  
> **Course:** CSET-211: Statistical Machine Learning  
> **Milestone:** Milestone 2 — Mid Progress Report (Target: 30% – 50% Project Scope)  
> **Repository:** [GitHub: Aarsi-Trivedi/Campus-IQ](https://github.com/Aarsi-Trivedi/Campus-IQ)

---

## 1. Project & Form Identification Details

| Form Field # | Form Question | Submitted Response |
| :--- | :--- | :--- |
| **1** | **Project Title** | **Campus IQ: An Interpretable Statistical Machine Learning System for Predicting Campus Resource Demand and Overcrowding** |
| **2** | **Enrollment No.: Member 1, Name** | **S25CSEU1882: AARSI TRIVEDI** (Project Lead) |
| **3** | **Enrollment No.: Member 2, Name** | **S25CSEU1868: ARJU** |
| **4** | **Enrollment No.: Member 3, Name** | **S25CSEU1873: ANGEL** |
| **5** | **Technology Used** | **Software** (Strict Classical Statistical Machine Learning — Zero Deep Learning / Neural Networks / LLMs) |
| **6** | **UN-SDG GOAL** | **SDG 11 — Sustainable Cities and Communities; SDG 12 — Responsible Consumption and Production** |
| **7** | **Dataset Collection (Provide Link)** | [https://github.com/Aarsi-Trivedi/Campus-IQ/blob/main/data/user_uploaded_campus_data.csv](https://github.com/Aarsi-Trivedi/Campus-IQ/blob/main/data/user_uploaded_campus_data.csv) |
| **8** | **Tentative AI/ML Model to be Used** | **The project uses strict classical statistical machine learning (no neural networks or LLMs) across continuous demand prediction (Linear Regression, Random Forest Regressor, Gradient Boosting) and overcrowding/risk classification (Logistic Regression, Random Forest Classifier) with K-Means clustering and PCA for campus activity patterns.** |

---

## 2. Milestone 2 Progress Status & Scope Demarcation

### Milestone Completion Metric
$$\mathbf{\text{Current Milestone Progress: }} \mathbf{38.5\%} \quad (\text{Target: } 30\% - 50\% \text{ Mid-Term Scope})$$

```
[████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 38.5% COMPLETED
```

### 12-Stage Pipeline Progress Audit

| Stage | Pipeline Stage Description | Weight | Status | Milestone Demarcation |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Problem Formulation, System Architecture & Scope Definition | 5.0% | **COMPLETED** | **Milestone 2 (Mid-Term)** |
| **2** | Multi-Facility Campus Data Collection & Integrity Verification | 10.0% | **COMPLETED** | **Milestone 2 (Mid-Term)** |
| **3** | Data Cleaning, Type Standardization & Missing Value Imputation | 5.0% | **COMPLETED** | **Milestone 2 (Mid-Term)** |
| **4** | In-Depth Exploratory Data Analysis (EDA) & Distribution Modeling | 5.0% | **COMPLETED** | **Milestone 2 (Mid-Term)** |
| **5** | Statistical Rigor: 1.5x IQR Outlier Analysis & Hypothesis Testing | 5.0% | **COMPLETED** | **Milestone 2 (Mid-Term)** |
| **6** | Domain Feature Engineering (Loads, Flags, SDG 12, CPI Formulation) | 5.0% | **COMPLETED** | **Milestone 2 (Mid-Term)** |
| **7** | Primary Target Baseline ML Models (Sports Demand & Overcrowding) | 3.5% | **COMPLETED** | **Milestone 2 (Mid-Term)** |
| **--** | **TOTAL MILESTONE 2 (MID-TERM EVALUATION)** | **38.5%** | **READY** | **Evaluated Scope** |
| 8 | Multi-Facility ML Models for Food Outlets (SDG 12 Waste/Surplus) | 12.0% | Planned | Milestone 3 (Final) |
| 9 | Multi-Facility ML Models for Library Study Spaces (SDG 11) | 10.0% | Planned | Milestone 3 (Final) |
| 10 | Unsupervised Activity Clustering & PCA Dimensionality Reduction | 10.0% | Planned | Milestone 3 (Final) |
| 11 | Campus Demand Flow Network & Spillover Modeling | 8.0% | Planned | Milestone 3 (Final) |
| 12 | Real-Time CPI Calculation & Lower-Demand Recommendation Engine | 10.0% | Planned | Milestone 3 (Final) |
| 13 | Interactive Student & Administration Production Web Dashboard | 11.5% | Planned | Milestone 3 (Final) |
| **--** | **TOTAL MILESTONE 3 (FINAL SUBMISSION)** | **61.5%** | **PLANNED** | **Final Semester Goal** |

---

## 3. Executive Problem Statement & UN-SDG Alignment

### 3.1 Real-World Problem
University campuses frequently experience acute spatial congestion and resource misallocation during peak hours. In particular, the **campus sports complex suffers severe overcrowding** during evening hours and tournament periods, resulting in equipment shortages, unsafe court conditions, and long waiting times. Concurrently, cafeteria kitchens struggle with volatile meal demand leading to preventable food waste, and library study halls become completely overwhelmed during midterm crunch weeks while remaining underutilized during regular periods.

### 3.2 Interconnected Campus Demand Flow
Rather than isolating facilities, Campus IQ investigates how student activity ripples through campus infrastructure over time:
$$\text{Campus Activity (Academic Schedule / Events)} \longrightarrow \text{Facility Demand} \longrightarrow \text{Congestion Risk} \longrightarrow \text{Actionable Recommendations}$$

### 3.3 UN Sustainable Development Goals (SDG) Alignment
1. **SDG 11 (Sustainable Cities and Communities — Target 11.7):**
   - Provides safe, equitable, and data-driven access to shared university physical infrastructure.
   - Relieves spatial congestion by estimating peak risk and redirecting students to lower-demand operating windows.
2. **SDG 12 (Responsible Consumption and Production — Target 12.3):**
   - Mitigates campus dining food waste by predicting meal demand and surplus/shortage risk quantities.
   - Provides cafeteria kitchen staff with calibrated batch-preparation targets within $\pm 5\%$ safety margins.

---

## 4. Dataset Ingestion & Quality Audit (Stage 2 & 3)

The dataset is hosted publicly in the project repository:
`data/user_uploaded_campus_data.csv` (Commit verified: 490 observations).

### 4.1 Schema Description
The dataset contains longitudinal records captured across time slots and academic calendar phases:

| Feature Name | Data Type | Operational Description |
| :--- | :--- | :--- |
| `date` | `datetime` | Calendar date (2026-08-03 to 2026-10-11, capturing regular & midterm phases) |
| `time_slot` | `object` | Operating interval (`08:00-10:00`, `10:00-12:00`, `12:00-14:00`, `14:00-16:00`, `16:00-18:00`, `18:00-20:00`, `20:00-22:00`) |
| `semester_phase` | `object` | Academic stage (`Regular`, `Midterm`, `Exam`) |
| `academic_workload` | `int64` | Ordinal scale (1 = Minimum stress, 5 = Maximum deadline crunch) |
| `classes_ending_nearby` | `int64` | Number of scheduled lectures concluding within 200m in the preceding 30 minutes |
| `campus_event_flag` | `int64` | Binary indicator (1 = University event active, 0 = Normal day) |
| `event_type` | `object` | Categorical descriptor (`Tournament`, `Cultural Fest`, `Hackathon`, `None`) |
| `sports_prev_crowd` | `int64` | Visitor count observed in the preceding operating interval (autoregressive cue) |
| `sports_visitors` | `int64` | **Primary Continuous Target:** Number of active sports complex visitors |
| `sports_capacity` | `int64` | Fixed physical facility throughput limit ($200$ visitors) |
| `sports_overcrowded` | `int64` | **Primary Binary Target:** Overcrowding flag (1 if Load $\ge 80\%$, 0 otherwise) |
| `library_occupancy` | `int64` | Observed headcount in primary study hall |
| `library_capacity` | `int64` | Fixed study seat capacity ($350$ seats) |
| `food_orders_demand` | `int64` | Cafeteria meal order volume during operating interval |
| `food_surplus_shortage_risk`| `int64` | Cafeteria kitchen balance status (1 = Shortage Risk, 0 = Balanced) |
| `campus_pulse_index` | `float64` | Normalized composite resource strain indicator ($0 - 100$) |

### 4.2 Data Integrity Audit
- **Total Records:** 490 rows
- **Duplicate Records:** 0 (Zero duplication detected)
- **Missing Values Audit:**
  - Numeric & operational features: **0 missing values (100% complete)**.
  - `event_type`: 450 null entries correspond exactly to intervals where `campus_event_flag == 0` (no campus event active). Imputed systematically with `'None'`.
- **Temporal Integrity:** Sorted chronologically from August 3, 2026 to October 11, 2026. Ensures that train/test splits have **zero lookahead data leakage**.

---

## 5. Domain Feature Engineering (Stage 6)

In compliance with Section 5 of the project proposal, domain-specific metrics were formulated:

### 5.1 Sports Complex Capacity Load & Overcrowding Flag
$$\text{Sports Load (\%)} = \left(\frac{\text{Sports Visitors}}{\text{Capacity}_{\text{sports}}}\right) \times 100 \quad (\text{Capacity} = 200)$$
$$\text{Sports Overcrowded Flag} = \begin{cases} 1 & \text{if Sports Load} \ge 80.0\% \\ 0 & \text{otherwise} \end{cases}$$

### 5.2 Food Outlets Waste & Shortage Equations (SDG 12 Target 12.3)
$$\text{Food Sold} = \min(\text{Prepared Quantity}, \text{Order Demand})$$
$$\text{Food Surplus Quantity} = \max(0, \text{Prepared Quantity} - \text{Food Sold})$$
$$\text{Food Shortage Quantity} = \max(0, \text{Order Demand} - \text{Prepared Quantity})$$

### 5.3 Campus Pulse Index (CPI) Formulation
A normalized composite metric ($0$ to $100$) capturing total multi-facility operational load:
$$\text{CPI} = 0.35 \cdot \text{SportsLoad} + 0.30 \cdot \text{LibraryLoad} + 0.25 \cdot \text{FoodNorm} + 0.10 \cdot \text{WorkloadScore}$$
Where:
- $\text{FoodNorm} = \min(100, (\text{Food Orders} / 300) \times 100)$
- $\text{WorkloadScore} \in \{30, 60, 90\}$ mapped from low, medium, and high academic strain.
- *Weight Rationale:* Sports complex ($0.35$) represents the tightest physical safety bottleneck; library ($0.30$) captures high-volume academic throughput; cafeteria ($0.25$) accounts for perishable waste; and academic workload ($0.10$) serves as the macro driver. $\sum w_i = 1.00$.

---

## 6. Statistical Rigor & Exploratory Data Analysis (Stage 4 & 5)

### 6.1 Comprehensive Descriptive Statistics Matrix
Evaluated across all 490 campus observations:

| Feature Name | Count | Mean | Std Dev | Median | Q25 | Q75 | IQR | Min | Max | Skewness |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `sports_visitors` | 490 | 51.3 | 31.1 | 42.0 | 25.0 | 83.0 | 58.0 | 6.0 | 130.0 | +0.38 |
| `sports_load_pct` | 490 | 42.7 | 25.9 | 35.0 | 20.8 | 69.2 | 48.3 | 5.0 | 108.3 | +0.38 |
| `food_orders_demand` | 490 | 78.3 | 41.8 | 62.5 | 45.0 | 117.0 | 72.0 | 15.0 | 187.0 | +0.43 |
| `food_surplus_qty` | 490 | 3.0 | 2.0 | 2.0 | 1.0 | 4.0 | 3.0 | 0.0 | 7.0 | +0.29 |
| `library_occupancy` | 490 | 56.5 | 41.0 | 43.5 | 29.2 | 69.0 | 39.8 | 10.0 | 196.0 | +1.69 |
| `campus_pulse_index` | 490 | 34.0 | 12.1 | 31.4 | 24.1 | 45.0 | 20.9 | 13.4 | 74.5 | +0.47 |

### 6.2 Outlier Analysis (1.5x IQR Rule)
- Sports Visitors: $Q_3 = 83.0$, $\text{IQR} = 58.0 \implies \text{Upper Fence} = 83.0 + 1.5(58.0) = 170.0$ visitors.
- Max observed visitors in dataset = $130$ visitors (load = $108.3\%$).
- **Methodological Rule (Section 7 of Proposal):** Outliers and spikes are **investigated and retained** rather than deleted, because real-world tournaments and cultural fests represent genuine high-impact operational surges that the statistical ML system must anticipate.

### 6.3 Formal Statistical Hypothesis Testing ($\alpha = 0.05$)
Conducted using both parametric (Welch's Two-Sample t-test) and non-parametric (Mann-Whitney U) tests with Cohen's $d$ effect sizes:

```
========================================================================================
TEST 1: Sports Complex Weekend vs. Weekday Demand
----------------------------------------------------------------------------------------
• Weekend Sample:  Mean = 60.3 visitors (std = 33.2, n = 140)
• Weekday Sample:  Mean = 47.6 visitors (std = 29.5, n = 350)
• Welch's t-test:        t = 4.1967  |  p-value = 3.71e-05
• Mann-Whitney U test:   U = 31798.0 |  p-value = 2.54e-07
• Effect Size (Cohen's d): 0.4145 (Moderate effect)
• Decision: REJECT NULL HYPOTHESIS (H0).
  Weekend sports attendance is significantly higher than weekday attendance (p < 0.001).
========================================================================================
TEST 2: Library Study Space Occupancy during Midterms vs. Regular Semester
----------------------------------------------------------------------------------------
• Midterm Sample:  Mean = 156.8 seats (std = 18.2, n = 56)
• Regular Sample:  Mean = 43.5 seats  (std = 20.8, n = 434)
• Welch's t-test:        t = 41.1962 |  p-value = 5.31e-51
• Mann-Whitney U test:   U = 24304.0 |  p-value = 3.64e-34
• Effect Size (Cohen's d): 5.7911 (Extremely large effect)
• Decision: REJECT NULL HYPOTHESIS (H0).
  Library demand surges by +260% during midterms, validating the need for study rerouting.
========================================================================================
TEST 3: Cafeteria Lunch Rush (12:00-14:00) Concentration (SDG 12 Stockout Risk)
----------------------------------------------------------------------------------------
• Lunch Rush Sample: Mean = 141.3 orders (std = 28.5, n = 70)
• Off-Peak Sample:   Mean = 67.8 orders  (std = 34.7, n = 420)
• Welch's t-test:        t = 27.5346 |  p-value = 7.33e-67
• Mann-Whitney U test:   U = 28421.5 |  p-value = 6.48e-36
• Effect Size (Cohen's d): 2.2275 (Large effect)
• Decision: REJECT NULL HYPOTHESIS (H0).
  Meal orders are severely concentrated during lunch, confirming food shortage risks.
========================================================================================
```

---

## 7. Baseline Machine Learning Models — Primary Target (Stage 7)

As designated in Section 1 of the project document, **overcrowding of the campus sports complex at peak times is the primary real-world problem**.

### 7.1 Train / Test Split Strategy
To eliminate temporal lookahead leakage, the 490 campus observations were partitioned strictly on a chronological basis:
- **Training Set:** 392 observations (80.0%)
- **Testing Set:** 98 observations (20.0%)

### 7.2 Regression Benchmarks: Sports Visitor Count
Target: Continuous visitor volume ($y \in [0, 200]$)

| Model Candidate | Model Family | MAE | RMSE | $R^2$ Score | Status |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Linear Regression** | Classical Parametric | 19.96 | 23.29 | 0.4061 | Baseline |
| **Random Forest Regressor** | Classical Ensemble | **6.60** | **10.30** | **0.8839** | **Selected Best (Mid-Term)** |

*Analysis:* Linear regression captures the global linear trend ($R^2 = 0.4061$). Random Forest Regressor demonstrates strong non-linear performance ($R^2 = 0.8839$, $\text{MAE} = 6.60$ visitors), capturing interaction effects between starting hour, classes ending nearby, and weekend indicators.

### 7.3 Classification Benchmarks: Sports Overcrowding Risk ($\ge 80\%$ Capacity)
Target: Binary overcrowding risk ($y \in \{0, 1\}$)

| Model Candidate | Accuracy | Precision | Recall | F1-Score | Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Logistic Regression** | 0.8571 | 0.3333 | 0.5556 | 0.4167 | Baseline |
| **Random Forest Classifier** | **0.9184** | **0.5333** | **0.8889** | **0.6667** | **Selected Best (Mid-Term)** |

### 7.4 Confusion Matrix (Random Forest Classifier on Test Set, $N=98$)
$$\begin{pmatrix} \text{True Negatives (TN) = 82} & \text{False Positives (FP) = 7} \\ \text{False Negatives (FN) = 1} & \text{True Positives (TP) = 8} \end{pmatrix}$$
- **Recall = 88.9%:** The classifier successfully catches 8 out of 9 critical overcrowding incidents.
- **Accuracy = 91.8%:** High overall diagnostic reliability for facility managers.

### 7.5 Feature Importance Attribution (Explainable Classical ML)
Deconstructing the Gini importance from the Random Forest Regressor:
1. `starting_hour`: **79.20%** (Evening hours 17:00-20:00 dominate attendance)
2. `is_midterm`: **4.63%** (Academic exams cause a significant drop in recreation)
3. `academic_workload`: **4.58%** (Direct inverse pressure on recreational sports)
4. `campus_event_flag`: **4.22%** (Campus tournaments trigger immediate attendee surges)
5. `day_of_week_num`: **2.09%** (Weekend vs weekday baseline variance)

---

## 8. Milestone 2 Verification & Reproducibility Guide

All deliverables for Milestone 2 can be verified directly:

### 1. Execute Terminal Evaluation Script
To run the automated Milestone 2 statistical evaluation and benchmark report:
```bash
python3 run_midterm_evaluation.py
```

### 2. Inspect Jupyter Notebook
Open and execute the pre-computed Milestone 2 notebook:
- **`Campus_IQ_Midterm_Evaluation.ipynb`** (Contains all 25 markdown and code cells with pre-computed tables, hypothesis test outputs, and visualizations).
- Or view the companion preprocessing notebook: **`Campus_IQ_PreProcessing_and_EDA.ipynb`**.

### 3. Verify Public GitHub Repository
- Dataset link verified: `https://github.com/Aarsi-Trivedi/Campus-IQ/blob/main/data/user_uploaded_campus_data.csv`

---

## 9. Milestone 3 (Final Submission) Work Plan & Roadmap (Remaining 61.5%)

| Phase | Milestone 3 Work Package | Target Deliverable | Expected Timeline |
| :---: | :--- | :--- | :---: |
| **Phase 1** | **Multi-Facility ML Modeling** | Ridge, Random Forest & Gradient Boosting for Food Outlets (SDG 12) and Library Study Spaces (SDG 11). | Weeks 9 – 10 |
| **Phase 2** | **Unsupervised Clustering & PCA** | K-Means clustering ($K=3$) with Silhouette analysis & 2D PCA projection for campus activity personas. | Weeks 10 – 11 |
| **Phase 3** | **Demand Flow Ripple Analysis** | Inter-facility cross-correlation and transition lag models (Sports $\leftrightarrow$ Food $\leftrightarrow$ Library). | Week 11 |
| **Phase 4** | **Recommender Engine & CPI Engine** | Dynamic best alternative time slot recommendation engine with percentage crowd reduction metrics. | Week 12 |
| **Phase 5** | **Production Web Dashboard** | Interactive browser portal with CPI gauge, scenario simulator, and facility management analytics. | Weeks 12 – 13 |
| **Phase 6** | **Final System Integration & Testing** | End-to-end automated testing, final documentation, and project defense presentation. | Week 14 |

---

*Report submitted by Aarsi Trivedi (S25CSEU1882), Arju (S25CSEU1868), and Angel (S25CSEU1873) for CSET-211: Statistical Machine Learning.*
