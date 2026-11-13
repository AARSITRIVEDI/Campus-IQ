# Campus IQ — Milestone 2 Presentation Slides Transcript & Speaker Notes

> **Course:** CSET-211: Statistical Machine Learning  
> **Milestone:** Milestone 2 — Mid Progress Report (Target: 30% – 50% Scope)  
> **Interactive Slide Deck:** Open [`Campus_IQ_Milestone2_Presentation.html`](Campus_IQ_Milestone2_Presentation.html) in your browser.  
> **Printable Academic Report:** Open [`Campus_IQ_Milestone2_Progress_Report.html`](Campus_IQ_Milestone2_Progress_Report.html) in your browser.

---

### Slide 1: Title & Team Metadata
* **Title:** Campus IQ: An Interpretable Statistical Machine Learning System for Predicting Campus Resource Demand and Overcrowding
* **Sub-title:** Project Milestone 2 — Mid Progress Evaluation (40% – 50% Scope)
* **Course:** CSET-211: Statistical Machine Learning
* **Team Members:**
  * Member 1 (Lead): S25CSEU1882 — AARSI TRIVEDI
  * Member 2: S25CSEU1868 — ARJU
  * Member 3: S25CSEU1873 — ANGEL
* **UN-SDG Alignment:** SDG 11 (Sustainable Cities) & SDG 12 (Responsible Consumption)
* **Repository:** `https://github.com/Aarsi-Trivedi/Campus-IQ`
* **Speaker Note:** *"Good morning/afternoon professors. Today we are presenting Milestone 2 for our Statistical Machine Learning project: Campus IQ. In this mid-term evaluation, we demonstrate our completed first phase (approximately 40% to 50% of the overall system pipeline), focusing on data collection, statistical rigor, EDA, and baseline ML models for the campus sports complex."*

---

### Slide 2: Problem Statement & Scope Control
* **Primary Real-World Problem:** Severe overcrowding at the campus sports complex during evening peak periods, leading to long queues, equipment shortages, and safety risks.
* **Campus Demand Flow:** Studying how student traffic flows across three interconnected areas rather than treated as isolated facilities:
  1. Sports Complex (Overcrowding & Capacity Management)
  2. Food Outlets (Cafeteria meal demand planning & waste prevention — SDG 12)
  3. Library Study Spaces (Exam crunch occupancy & satellite study space rerouting — SDG 11)
* **Core Principle:** $\text{Campus Activity} \longrightarrow \text{Demand} \longrightarrow \text{Risk} \longrightarrow \text{Recommendation}$
* **Methodological Rule:** Strict classical statistical machine learning (zero deep learning or LLMs) prioritizing interpretability and explainability.
* **Speaker Note:** *"Rather than viewing gym congestion, cafeteria lunch lines, and library exam crunches separately, Campus IQ models them as an interconnected demand flow. We deliberately avoid black-box neural networks in favor of transparent classical ML."*

---

### Slide 3: Milestone Progress Breakdown (50.0% Scope — Phase 1 Complete)
* **Completed Stages (Milestone 2 Scope):**
  * Stage 1: Problem Formulation, System Architecture & Multi-Facility Scope — 10.0%
  * Stage 2: Multi-Facility Campus Data Collection & Audit (490 records) — 10.0%
  * Stage 3: Data Cleaning, Temporal Preprocessing & Imputation — 10.0%
  * Stage 4: Statistical Analysis: Descriptive Stats, 1.5x IQR & Hypothesis Tests — 10.0%
  * Stage 5: Domain Feature Engineering & Primary Baseline ML Models (Sports) — 10.0%
  * **Current Total: 50.0% Completed (Phase 1 Complete / Evaluation Ready)**
* **Planned Stages (Milestone 3 / Final Submission Scope):**
  * Stages 6 & 7: Food Outlets ML (SDG 12) & Library Study Space ML (SDG 11) — 20.0%
  * Stages 8 & 9: K-Means Clustering + PCA & Campus Demand Flow Ripple Network — 15.0%
  * Stages 10 & 11: Real-Time CPI Calculation Engine & Production Web Portal — 15.0%
  * **Milestone 3 Final Total: 50.0% Planned**
* **Speaker Note:** *"As shown in our progress matrix, we have completed the full first phase representing exactly 50% of the overall system pipeline. This covers data collection, thorough statistical analysis, formal hypothesis testing, and operational baseline ML models on our primary target. The remaining 50% covers multi-facility models, unsupervised clustering, and the full web dashboard, which are scheduled for our final defense."*

---

### Slide 4: Campus Data Collection & Quality Audit
* **Dataset Source:** `data/user_uploaded_campus_data.csv` (490 longitudinal records).
* **Integrity Audit:**
  * 0 duplicate rows detected.
  * 0 missing values across all numerical and operational columns.
  * Non-event intervals (450 rows where campus event flag = 0) systematically imputed with `'None'`.
* **Zero Lookahead Data Leakage:**
  * Chronological 80/20 train/test partition (392 train observations, 98 test observations).
  * Prevents future information from bleeding into historical models.
* **Speaker Note:** *"We collected and audited 490 chronological campus observations. Crucially, to prevent data leakage, we partitioned the data chronologically rather than using a randomized split, ensuring our models predict future time slots using only past observations."*

---

### Slide 5: Domain Feature Engineering & Formulations
* **Sports Load (%):** $(\text{Sports Visitors} / 200) \times 100$
* **Overcrowding Risk Flag:** $1 \text{ if Sports Load} \ge 80.0\%, \text{ else } 0$
* **Cafeteria Food Waste (SDG 12):** $\text{Food Sold} = \min(\text{Prepared}, \text{Demand}); \text{Surplus} = \max(0, \text{Prepared} - \text{Sold})$
* **Library Load (%):** $(\text{Library Occupancy} / 350) \times 100$
* **Campus Pulse Index (CPI):** $0.35 \times \text{SportsLoad} + 0.30 \times \text{LibraryLoad} + 0.25 \times \text{FoodNorm} + 0.10 \times \text{Workload}$
* **Speaker Note:** *"We engineered key domain metrics, including capacity loads, overcrowding thresholds, and the normalized Campus Pulse Index, where the sports complex receives the highest operational weight due to safety constraints."*

---

### Slide 6: Descriptive Statistics Matrix
* **Key Distributions:**
  * Sports Visitors: Mean = 51.3, Median = 42.0, Std = 31.1, IQR = 58.0, Max = 130.0 (Load = 108.3%).
  * Sports Load: Mean = 42.7%, Skewness = +0.38 (moderate positive skew).
  * Food Orders: Mean = 78.3 orders, IQR = 72.0, Max = 187.0 orders.
  * Library Occupancy: Mean = 56.5 seats, Max = 196.0 seats, Skewness = +1.69 (high concentration during exam weeks).
  * Campus Pulse Index: Mean = 34.0, Median = 31.4, Max = 74.5.
* **Speaker Note:** *"Our descriptive statistics reveal right-skewed demand across campus facilities, driven by severe evening rush hours and exam periods."*

---

### Slide 7: Outlier Analysis (1.5x IQR Rule) & Contextualization
* **Tukey's Fences:** $Q_3 + 1.5 \times \text{IQR} = 83.0 + 1.5(58.0) = 170.0$ visitors.
* **Maximum Observed Value:** 130 visitors (108.3% load).
* **Domain Justification (Section 7):** Spikes represent genuine university tournaments and cultural fests.
* **Methodological Decision:** Investigated and retained rather than automatically deleted, ensuring ML models learn to anticipate real surges.
* **Speaker Note:** *"In accordance with Section 7 of our project specification, we investigated outlier spikes rather than deleting them. In operational campus management, tournaments and fests are real events that our model must anticipate."*

---

### Slide 8: Formal Statistical Hypothesis Testing ($\alpha = 0.05$)
* **Hypothesis 1 (Weekend Sports Surge):** Weekend Mean = 60.3 vs Weekday Mean = 47.6.
  * Welch's $t = 4.1967$ ($p = 3.71 \times 10^{-5}$), Mann-Whitney $U = 31798.0$, Cohen's $d = 0.4145$.
  * **Decision:** Reject $H_0$ ($p < 0.001$). Weekend sports attendance is significantly higher.
* **Hypothesis 2 (Library Exam Surge):** Midterm Mean = 156.8 seats vs Regular Mean = 43.5 seats.
  * Welch's $t = 41.1962$ ($p = 5.31 \times 10^{-51}$), Mann-Whitney $U = 24304.0$, Cohen's $d = 5.7911$.
  * **Decision:** Reject $H_0$ ($p < 0.001$). Library occupancy surges by +260% during midterms.
* **Hypothesis 3 (Cafeteria Lunch Rush):** Lunch (12-14) Mean = 141.3 vs Off-Peak Mean = 67.8 orders.
  * Welch's $t = 27.5346$ ($p = 7.33 \times 10^{-67}$), Mann-Whitney $U = 28421.5$, Cohen's $d = 2.2275$.
  * **Decision:** Reject $H_0$ ($p < 0.001$). Dining demand is heavily concentrated during lunch rush.
* **Speaker Note:** *"All three formal hypothesis tests rejected the null hypothesis with p-values far below 0.001, proving that academic schedules, weekends, and lunch periods cause statistically significant demand shocks."*

---

### Slide 9: Primary Baseline ML — Regression Benchmarks
* **Continuous Target:** Sports Visitor Count (Test Set $N=98$).
* **Linear Regression (Parametric Baseline):** $\text{MAE} = 19.96$, $\text{RMSE} = 23.29$, $R^2 = 0.4061$.
* **Random Forest Regressor (Ensemble Baseline):** $\text{MAE} = \mathbf{6.60}$, $\text{RMSE} = \mathbf{10.30}$, $\mathbf{R^2 = 0.8839}$.
* **Improvement:** Random Forest reduces Mean Absolute Error by **66.9%** and achieves an $R^2$ of 0.8839 by modeling non-linear schedule interactions.
* **Speaker Note:** *"For our primary regression task, Random Forest significantly outperformed Linear Regression, reducing prediction error down to 6.6 visitors and explaining 88.4% of the variance."*

---

### Slide 10: Primary Baseline ML — Classification & Confusion Matrix
* **Binary Target:** Overcrowding Risk Flag ($\ge 80\%$ Capacity).
* **Logistic Regression:** $\text{Accuracy} = 85.7\%$, $\text{Precision} = 33.3\%$, $\text{Recall} = 55.6\%$, $\text{F1} = 0.4167$.
* **Random Forest Classifier:** $\mathbf{\text{Accuracy} = 91.8\%}$, $\text{Precision} = 53.3\%$, $\mathbf{\text{Recall} = 88.9\%}$, $\mathbf{\text{F1} = 0.6667}$.
* **Confusion Matrix ($N=98$):**
  $$\text{True Negatives} = 82, \quad \text{False Positives} = 7, \quad \text{False Negatives} = 1, \quad \text{True Positives} = 8$$
* **Clinical / Safety Value:** High recall (88.9%) ensures that 8 out of 9 critical overcrowding incidents are anticipated in advance.
* **Speaker Note:** *"In classification, Random Forest achieved 91.8% accuracy and 88.9% recall, missing only 1 single overcrowding incident out of 9 on the test set."*

---

### Slide 11: Feature Importance Attribution (Explainable ML)
* **Gini Importance Breakdown:**
  1. `starting_hour`: **79.20%** (Evening hours 17:00–20:00 dominate attendance)
  2. `is_midterm`: **4.63%** (Exams cause a sharp drop in recreational sports)
  3. `academic_workload`: **4.58%** (Direct inverse pressure on recreation)
  4. `campus_event_flag`: **4.22%** (Tournament spectator influx triggers immediate surges)
  5. `day_of_week_num`: **2.09%** (Weekend vs weekday variance)
* **Operational Benefit:** Facility managers understand *why* overcrowding was predicted, allowing targeted schedule adjustments.
* **Speaker Note:** *"Our explainability analysis proves that starting hour, exam periods, and tournaments are the primary drivers of sports congestion."*

---

### Slide 12: Milestone 3 Roadmap & Future Scope (Remaining 50%)
* **Phase 1 (Weeks 9–10):** Multi-facility ML modeling for Food Outlets (SDG 12) and Library (SDG 11).
* **Phase 2 (Weeks 10–11):** Unsupervised K-Means Clustering ($K=3$) and 2D PCA for campus activity personas.
* **Phase 3 (Week 11):** Campus Demand Flow Ripple Network modeling lead-lag cross-facility cascades.
* **Phase 4 (Week 12):** Real-time CPI Engine & dynamic lower-demand alternative slot recommender.
* **Phase 5 (Weeks 12–13):** Full production interactive web dashboard.
* **Phase 6 (Week 14):** Final defense, end-to-end testing, and project submission.
* **Speaker Note:** *"To conclude, Milestone 2 has established a strong statistical and machine learning foundation. In Milestone 3, we will complete the remaining 50% across multi-facility modeling, clustering, and the full interactive dashboard. Thank you, and we welcome your questions!"*
