# Campus IQ: An Interpretable Statistical Machine Learning System for Predicting Campus Resource Demand and Overcrowding

> **Project Milestone 2: Mid Progress Evaluation (38.5% Scope Completed)**  
> **Course:** Statistical Machine Learning (CSET-211)  
> **Team Members:**  
> • **Member 1 (Lead):** S25CSEU1882 — AARSI TRIVEDI  
> • **Member 2:** S25CSEU1868 — ARJU  
> • **Member 3:** S25CSEU1873 — ANGEL  
> **UN-SDG Alignment:** SDG 11 (Sustainable Cities and Communities) & SDG 12 (Responsible Consumption and Production)  
> **Dataset Link:** [`data/user_uploaded_campus_data.csv`](https://github.com/Aarsi-Trivedi/Campus-IQ/blob/main/data/user_uploaded_campus_data.csv) (490 observations)  
> **Tentative ML Models:** Strict classical statistical machine learning (Linear Regression, Random Forest, Gradient Boosting, Logistic Regression, K-Means Clustering, PCA).

---

## 1. Mid-Term Evaluation Progress Status (38.5% Scope)

$$\mathbf{\text{Current Milestone Progress: }} \mathbf{38.5\%} \quad (\text{Target: } 30\% - 50\% \text{ Mid-Term Scope})$$

```
[████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 38.5% COMPLETED
```

In strict compliance with Milestone 2 guidelines, this repository presents **38.5% completion** of the full 12-stage Campus IQ pipeline:

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

## 2. Quick Start: How to Run the Mid-Term Evaluation

### Option 1: Run the Interactive Terminal Evaluation Benchmark
Execute the automated Milestone 2 runner to inspect data ingestion, statistical hypothesis tests, baseline model benchmarks, and confusion matrices:
```bash
python3 run_midterm_evaluation.py
```

### Option 2: Run the Automated Milestone 2 Unit Test Suite
Verify that all 5 milestone tests (dataset integrity, zero data leakage, feature engineering, hypothesis testing, and baseline model scoring) pass:
```bash
python3 test_midterm_milestone.py
```

### Option 3: Inspect the Milestone 2 Jupyter Notebooks
- **[`Campus_IQ_Midterm_Evaluation.ipynb`](Campus_IQ_Midterm_Evaluation.ipynb):** Comprehensive 25-cell executed notebook containing all preprocessing steps, EDA distributions, IQR outlier boxplots, correlation heatmaps, hypothesis tests, and primary baseline machine learning models with plots.
- **[`Campus_IQ_PreProcessing_and_EDA.ipynb`](Campus_IQ_PreProcessing_and_EDA.ipynb):** Companion notebook focused on statistical preprocessing and exploratory analysis.
- **[`MIDTERM_PROGRESS_REPORT.md`](MIDTERM_PROGRESS_REPORT.md):** Complete academic written report matching the submission form.

---

## 3. Project Overview & Scope Control

Campus IQ analyzes historical campus activity patterns and predicts resource demand, overcrowding, and resource-related risks across three interconnected campus zones:
1. **Sports Complex (Primary Focus):** Mitigates severe peak-hour overcrowding, estimates visitor counts and court loads, predicts overcrowding risk ($\ge 80\%$ capacity), and recommends lower-demand alternate time slots.
2. **Food Outlets (SDG 12):** Forecasts meal demand, calculates food surplus/shortage risks, and minimizes cafeteria food waste.
3. **Library & Study Spaces (SDG 11):** Analyzes study seat occupancy and identifies exam crunch periods.

### Methodological Principles
- **Core Principle:** $\text{Campus Activity} \longrightarrow \text{Demand} \longrightarrow \text{Risk} \longrightarrow \text{Recommendation}$
- **Deliberate Classical ML Focus:** Strictly avoids deep learning, neural networks, or opaque LLMs in favor of transparent, interpretable statistical algorithms.
- **Zero Lookahead Leakage:** Uses strict chronological 80/20 train-test splits.

---

## 4. Mathematical Formulations & Derived Metrics

1. **Sports Complex Load (%):**
   $$\text{Sports Load (\%)} = \left(\frac{\text{Sports Visitors}}{\text{Capacity}_{\text{sports}}}\right) \times 100 \quad (\text{Capacity} = 200)$$
2. **Sports Overcrowding Flag (Classification Target):**
   $$\text{Overcrowded Flag} = \begin{cases} 1 & \text{if Sports Load} \ge 80.0\% \\ 0 & \text{otherwise} \end{cases}$$
3. **Food Waste & Shortage Metrics (SDG 12 Target 12.3):**
   $$\text{Food Sold} = \min(\text{Prepared Quantity}, \text{Order Demand})$$
   $$\text{Food Surplus Quantity} = \max(0, \text{Prepared Quantity} - \text{Food Sold})$$
   $$\text{Food Shortage Quantity} = \max(0, \text{Order Demand} - \text{Prepared Quantity})$$
4. **Library Load (%):**
   $$\text{Library Load (\%)} = \left(\frac{\text{Library Occupancy}}{\text{Capacity}_{\text{library}}}\right) \times 100 \quad (\text{Capacity} = 350)$$
5. **Campus Pulse Index (CPI):**
   $$\text{CPI} = 0.35 \cdot \text{SportsLoad} + 0.30 \cdot \text{LibraryLoad} + 0.25 \cdot \text{FoodNorm} + 0.10 \cdot \text{WorkloadScore}$$

---

## 5. Statistical Rigor & Hypothesis Testing

Evaluated on 490 campus observations at $\alpha = 0.05$ using parametric (Welch's t-test) and non-parametric (Mann-Whitney U) tests with Cohen's $d$ effect sizes:

1. **Hypothesis 1 (Sports Weekend Surge):**
   - *Test:* Weekend sports visitor traffic vs. weekday traffic ($H_0: \mu_{\text{weekend}} = \mu_{\text{weekday}}$)
   - *Result:* $t = 4.1967$ ($p = 3.71 \times 10^{-5}$), Mann-Whitney $U = 31798.0$ ($p = 2.54 \times 10^{-7}$), Cohen's $d = 0.4145$.
   - *Decision:* **Reject $H_0$**. Weekend sports attendance is significantly higher.
2. **Hypothesis 2 (Library Midterm Crunch):**
   - *Test:* Library occupancy during midterms vs. regular semester ($H_0: \mu_{\text{midterm}} = \mu_{\text{regular}}$)
   - *Result:* $t = 41.1962$ ($p = 5.31 \times 10^{-51}$), Mann-Whitney $U = 24304.0$ ($p = 3.64 \times 10^{-34}$), Cohen's $d = 5.7911$.
   - *Decision:* **Reject $H_0$**. Library demand surges by $+260\%$ during midterm periods.
3. **Hypothesis 3 (Cafeteria Lunch Stockout Risk):**
   - *Test:* Lunch rush order volume (12:00-14:00) vs. off-peak slots ($H_0: \mu_{\text{lunch}} = \mu_{\text{offpeak}}$)
   - *Result:* $t = 27.5346$ ($p = 7.33 \times 10^{-67}$), Mann-Whitney $U = 28421.5$ ($p = 6.48 \times 10^{-36}$), Cohen's $d = 2.2275$.
   - *Decision:* **Reject $H_0$**. Meal orders are highly concentrated at lunch, confirming acute stockout risk.

---

## 6. Primary Focus Baseline Machine Learning Models (Sports Complex)

Evaluated on an isolated chronological test split (20%, 98 observations):

### Regression (Continuous Sports Visitor Count)
| Model Candidate | Model Family | MAE | RMSE | $R^2$ Score | Status |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Linear Regression** | Classical Parametric | 19.96 | 23.29 | 0.4061 | Baseline |
| **Random Forest Regressor** | Classical Ensemble | **6.60** | **10.30** | **0.8839** | **Selected Best (Mid-Term)** |

### Classification (Sports Overcrowding Risk $\ge 80\%$)
| Model Candidate | Model Family | Accuracy | Precision | Recall | F1-Score | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Logistic Regression** | Classical Parametric | 0.8571 | 0.3333 | 0.5556 | 0.4167 | Baseline |
| **Random Forest Classifier** | Classical Ensemble | **0.9184** | **0.5333** | **0.8889** | **0.6667** | **Selected Best (Mid-Term)** |

### Confusion Matrix (Random Forest Classifier on Test Set, $N=98$)
$$\begin{pmatrix} \text{True Negatives (TN) = 82} & \text{False Positives (FP) = 7} \\ \text{False Negatives (FN) = 1} & \text{True Positives (TP) = 8} \end{pmatrix}$$
- **Recall = 88.9%:** Effectively detects 8 out of 9 critical overcrowding incidents.
- **Accuracy = 91.8%:** High overall diagnostic reliability.

### Feature Importance Attribution (Explainable ML)
1. `starting_hour`: **79.20%**
2. `is_midterm`: **4.63%**
3. `academic_workload`: **4.58%**
4. `campus_event_flag`: **4.22%**
5. `day_of_week_num`: **2.09%**

---

## 7. Project File Structure (Milestone 2 Setup)

```
campus_iq/
├── data/
│   ├── user_uploaded_campus_data.csv   # 490 primary verified campus observations
│   ├── user_uploaded_campus_data.xlsx  # Excel master source
│   ├── train_dataset.csv               # 392 training observations (80%)
│   └── test_dataset.csv                # 98 testing observations (20%)
├── Campus_IQ_Midterm_Evaluation.ipynb  # Primary executed Milestone 2 notebook (25 cells)
├── Campus_IQ_PreProcessing_and_EDA.ipynb # Companion Preprocessing & EDA notebook
├── MIDTERM_PROGRESS_REPORT.md          # Formal academic progress report (38.5% scope)
├── run_midterm_evaluation.py           # Standalone Milestone 2 terminal benchmark runner
├── test_midterm_milestone.py           # Automated unit test suite for Milestone 2
├── src/                                # Modular architecture (cleaning, stats, models)
├── web/                                # Future scope: Interactive dashboard prototypes
├── requirements.txt                    # Project dependencies
└── README.md                           # System documentation & milestone demarcation
```

---

## 8. Milestone 3 Roadmap (Final 61.5% Scope)

The remaining 61.5% of the system pipeline will be completed for the Final Project Submission:
- **Phase 1:** Multi-Facility ML for Food Outlets (SDG 12) & Library Study Spaces (SDG 11).
- **Phase 2:** Unsupervised K-Means Clustering ($K=3$) & 2D PCA Dimensionality Reduction.
- **Phase 3:** Cross-Facility Demand Flow Ripple Network.
- **Phase 4:** Real-Time CPI Engine & Actionable Time Slot Recommender.
- **Phase 5:** Production Interactive Web Dashboard for Students and Administration.
- **Phase 6:** Final Defense & Comprehensive Documentation.
