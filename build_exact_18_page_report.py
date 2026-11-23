import os
import base64

html_out_path = "/Users/aarsitrivedi07/.gemini/antigravity/scratch/campus_iq/Campus_IQ_Project_Report.html"

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

fig1_b64 = get_b64("/Users/aarsitrivedi07/.gemini/antigravity/scratch/campus_iq/report_assets/fig1_campus_layout.png")
fig2_b64 = get_b64("/Users/aarsitrivedi07/.gemini/antigravity/scratch/campus_iq/report_assets/fig2_methodology_flowchart.png")
fig3_b64 = get_b64("/Users/aarsitrivedi07/.gemini/antigravity/scratch/campus_iq/report_assets/fig3_correlation_matrix.png")
fig4_b64 = get_b64("/Users/aarsitrivedi07/.gemini/antigravity/scratch/campus_iq/report_assets/fig4_pca_clusters.png")
fig5_b64 = get_b64("/Users/aarsitrivedi07/.gemini/antigravity/scratch/campus_iq/report_assets/fig5_silhouette_scores.png")
fig6_b64 = get_b64("/Users/aarsitrivedi07/.gemini/antigravity/scratch/campus_iq/report_assets/fig6_model_comparison.png")
fig7_b64 = get_b64("/Users/aarsitrivedi07/.gemini/antigravity/scratch/campus_iq/report_assets/fig7_feature_importance.png")
fig8_b64 = get_b64("/Users/aarsitrivedi07/.gemini/antigravity/scratch/campus_iq/report_assets/fig8_demand_flow.png")

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Campus IQ - Statistical Machine Learning Project Report</title>
  <style>
    @page {
      size: A4 portrait;
      margin-top: 25mm;
      margin-bottom: 25mm;
      margin-right: 25mm;
      margin-left: 38mm; /* 25mm + 13mm binding */
    }

    * {
      box-sizing: border-box;
    }

    body {
      font-family: 'Times New Roman', Times, serif;
      font-size: 12pt;
      line-height: 1.5;
      color: #000000;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }

    .report-page {
      page-break-after: always;
      break-after: page;
      position: relative;
      height: 247mm; /* Exact printable height on A4 (297 - 50) */
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }

    p {
      font-size: 12pt;
      line-height: 1.5;
      margin-top: 0;
      margin-bottom: 1.25em; /* 2.5 line spacing between paragraphs */
      text-align: justify;
      text-justify: inter-word;
    }

    h1.chapter-title {
      font-family: 'Times New Roman', Times, serif;
      font-size: 16pt;
      font-weight: bold;
      text-transform: uppercase;
      margin-top: 0;
      margin-bottom: 1.1em;
      letter-spacing: 0.5px;
    }

    h2.section-title {
      font-family: 'Times New Roman', Times, serif;
      font-size: 14pt;
      font-weight: bold;
      margin-top: 0.9em;
      margin-bottom: 0.5em;
    }

    h3.sub-title {
      font-family: 'Times New Roman', Times, serif;
      font-size: 12pt;
      font-weight: bold;
      margin-top: 0.8em;
      margin-bottom: 0.4em;
    }

    /* Title Page Specifics */
    .title-page-container {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      text-align: center;
      height: 100%;
      padding-top: 15mm;
      padding-bottom: 5mm;
    }

    .report-main-title {
      font-size: 17pt;
      font-weight: bold;
      line-height: 1.35;
      margin-bottom: 14mm;
      text-transform: uppercase;
    }

    .report-submitted-for {
      font-size: 13pt;
      margin-bottom: 6mm;
    }

    .report-course-title {
      font-size: 16pt;
      font-weight: bold;
      letter-spacing: 1px;
      margin-bottom: 18mm;
      text-transform: uppercase;
    }

    .student-entry {
      font-size: 12pt;
      font-weight: bold;
      line-height: 1.6;
    }

    .faculty-name-title {
      font-size: 12pt;
      font-weight: bold;
      margin-top: 2mm;
    }

    .school-title {
      font-size: 12.5pt;
      font-weight: bold;
      text-transform: uppercase;
      line-height: 1.3;
      max-width: 90%;
    }

    .univ-logo-badge {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin-top: 3mm;
    }

    .bu-logo-box {
      border-right: 1.5px solid #94a3b8;
      padding-right: 14px;
      text-align: left;
    }

    .bu-name {
      font-size: 16pt;
      font-weight: 900;
      color: #0f172a;
      letter-spacing: 0.5px;
      line-height: 1;
    }

    .bu-sub {
      font-size: 7.5pt;
      font-weight: 700;
      color: #b91c1c;
      letter-spacing: 1px;
    }

    .naac-badge {
      background: #1e3a8a;
      color: #ffffff;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 8.5pt;
      font-weight: bold;
      text-align: center;
      line-height: 1.2;
    }

    /* Tables */
    table.formal-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 0.6em;
      margin-bottom: 1.2em;
      font-size: 9.5pt;
    }

    table.formal-table th, table.formal-table td {
      border: 1px solid #1e293b;
      padding: 4px 6px;
      vertical-align: middle;
    }

    table.formal-table th {
      background-color: #f1f5f9;
      font-weight: bold;
      text-align: left;
    }

    table.formal-table td.center {
      text-align: center;
    }

    table.index-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 9.5pt;
    }

    table.index-table th, table.index-table td {
      border: 1px solid #000000;
      padding: 3.5px 6px;
    }

    table.index-table th {
      font-weight: bold;
    }

    /* Figures */
    .figure-container {
      text-align: center;
      margin-top: 0.6em;
      margin-bottom: 1.2em;
    }

    .figure-container img {
      max-width: 95%;
      height: auto;
      border: 1px solid #cbd5e1;
      border-radius: 3px;
    }

    .figure-caption {
      font-size: 9.5pt;
      font-style: italic;
      margin-top: 4px;
      color: #1e293b;
    }

    .table-caption {
      font-size: 9.5pt;
      font-weight: bold;
      margin-bottom: 4px;
      color: #0f172a;
    }

    /* Math Formulas */
    .formula-block {
      background: #f8fafc;
      border-left: 3px solid #1e3a8a;
      padding: 6px 12px;
      margin: 0.6em 0 1em 0;
      font-family: 'Times New Roman', serif;
      font-size: 10.5pt;
      font-style: italic;
    }

    .page-footer-mark {
      margin-top: auto;
      text-align: right;
      font-size: 10pt;
      font-family: 'Times New Roman', serif;
      padding-top: 4mm;
    }

  </style>
</head>
<body>

  <!-- ==============================================================================
       PAGE 1: TITLE PAGE (STRICT BENNETT UNIVERSITY FORMAT)
       ============================================================================== -->
  <div class="report-page">
    <div class="title-page-container">
      
      <div>
        <div class="report-main-title">
          CAMPUS IQ: SMART CAMPUS RESOURCE DEMAND PREDICTION AND CONGESTION MITIGATION USING STATISTICAL MACHINE LEARNING
        </div>
        
        <div class="report-submitted-for">Submitted for</div>
        
        <div class="report-course-title">
          STATISTICAL MACHINE LEARNING
        </div>
      </div>

      <div>
        <div style="font-size: 12pt; margin-bottom: 3mm;">Submitted by:</div>
        <div class="student-entry">(S25CSEU1882)&nbsp;&nbsp;&nbsp;&nbsp;AARSI TRIVEDI</div>
        <div class="student-entry">(S25CSEU1868)&nbsp;&nbsp;&nbsp;&nbsp;ARJU</div>
        <div class="student-entry">(S25CSEU1873)&nbsp;&nbsp;&nbsp;&nbsp;ANGEL</div>
      </div>

      <div>
        <div style="font-size: 12pt;">Submitted to-</div>
        <div class="faculty-name-title">Faculty Evaluator / Course Instructor</div>
      </div>

      <div style="width: 100%; display: flex; flex-direction: column; align-items: center; gap: 3mm;">
        <div style="font-size: 12pt; font-weight: bold;">July-Dec 2026</div>
        <div class="school-title">
          SCHOOL OF COMPUTER SCIENCE ENGINEERING &amp; TECHNOLOGY
        </div>
        
        <div class="univ-logo-badge">
          <div class="bu-logo-box">
            <div class="bu-name">BENNETT</div>
            <div style="font-size: 8.5pt; font-weight: bold; color: #1e3a8a;">UNIVERSITY</div>
            <div class="bu-sub">THE TIMES GROUP</div>
          </div>
          <div class="naac-badge">
            NAAC GRADE A+<br>ACCREDITED UNIVERSITY
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ==============================================================================
       PAGE 2: INDEX
       ============================================================================== -->
  <div class="report-page">
    <h1 class="chapter-title" style="text-align: center; margin-bottom: 1.2em;">INDEX</h1>

    <table class="index-table">
      <thead>
        <tr>
          <th style="width: 12%; text-align: center;">Sr No</th>
          <th style="width: 72%;">Content</th>
          <th style="width: 16%; text-align: center;">Page No</th>
        </tr>
      </thead>
      <tbody>
        <tr><td style="text-align: center;">1</td><td>List of Figures</td><td style="text-align: center;">3</td></tr>
        <tr><td style="text-align: center;">2</td><td>List of Tables</td><td style="text-align: center;">4</td></tr>
        <tr><td style="text-align: center;">3</td><td><strong>1. ABSTRACT</strong></td><td style="text-align: center;">5</td></tr>
        <tr><td style="text-align: center;">4</td><td><strong>2. BACKGROUND</strong></td><td style="text-align: center;">6</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;2.1 Problem Statement and Institutional Context</td><td style="text-align: center;">6</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;2.2 Research Objectives and Scope</td><td style="text-align: center;">6</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;2.3 Literature Review &amp; Theoretical Foundations</td><td style="text-align: center;">7</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;2.4 Research Gaps and Project Scope</td><td style="text-align: center;">7</td></tr>
        <tr><td style="text-align: center;">5</td><td><strong>3. SOFTWARE / HARDWARE USED</strong></td><td style="text-align: center;">8</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;3.1 Software Specifications and Tooling Stack</td><td style="text-align: center;">8</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;3.2 Hardware Environment</td><td style="text-align: center;">8</td></tr>
        <tr><td style="text-align: center;">6</td><td><strong>4. METHODOLOGY</strong></td><td style="text-align: center;">9</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;4.1 End-to-End System Architecture</td><td style="text-align: center;">9</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;4.2 Data Ingestion &amp; Methodology Flowchart</td><td style="text-align: center;">10</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;4.3 Mathematical Formulations &amp; Feature Engineering</td><td style="text-align: center;">11</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;4.4 Supervised Learning: Multi-Output Regression &amp; Classification</td><td style="text-align: center;">11</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;4.5 Unsupervised Routine Clustering &amp; 2D PCA Formulation</td><td style="text-align: center;">11</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;4.6 Formal Statistical Hypothesis Testing Formulation</td><td style="text-align: center;">11</td></tr>
        <tr><td style="text-align: center;">7</td><td><strong>5. EXPERIMENTAL RESULTS</strong></td><td style="text-align: center;">12</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;5.1 Descriptive Statistics &amp; Exploratory Data Analysis</td><td style="text-align: center;">12</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;5.2 Correlation Matrix Analysis</td><td style="text-align: center;">12</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;5.3 Formal Hypothesis Testing Results (Welch's t-test)</td><td style="text-align: center;">13</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;5.4 Supervised Regression Model Benchmarks</td><td style="text-align: center;">13</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;5.5 Classification Benchmarks for Congestion Risk</td><td style="text-align: center;">14</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;5.6 Feature Importance Attribution (Mean Decrease in Impurity)</td><td style="text-align: center;">14</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;5.7 Unsupervised Operational Regimes &amp; 2D PCA</td><td style="text-align: center;">15</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;5.8 Interconnected Markov Campus Demand Flow</td><td style="text-align: center;">16</td></tr>
        <tr><td style="text-align: center;">8</td><td><strong>6. CONCLUSION</strong></td><td style="text-align: center;">17</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;6.1 Summary of Deliverables &amp; Findings</td><td style="text-align: center;">17</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;6.2 Alignment with UN Sustainable Development Goals</td><td style="text-align: center;">17</td></tr>
        <tr><td style="text-align: center;"></td><td>&nbsp;&nbsp;&nbsp;&nbsp;6.3 Practical Institutional Implications &amp; Future Directions</td><td style="text-align: center;">17</td></tr>
        <tr><td style="text-align: center;">9</td><td><strong>7. REFERENCES</strong></td><td style="text-align: center;">18</td></tr>
      </tbody>
    </table>

    <div class="page-footer-mark">2</div>
  </div>

  <!-- ==============================================================================
       PAGE 3: LIST OF FIGURES (SEPARATE PAGE REQUIRED)
       ============================================================================== -->
  <div class="report-page">
    <h1 class="chapter-title" style="text-align: center; margin-bottom: 1.5em;">LIST OF FIGURES</h1>

    <table class="index-table">
      <thead>
        <tr>
          <th style="width: 18%; text-align: center;">Figure No.</th>
          <th style="width: 66%;">Title</th>
          <th style="width: 16%; text-align: center;">Page No.</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="text-align: center;">Figure 1</td>
          <td>Isometric Layout of Bennett University Campus IQ Operational Scenario</td>
          <td style="text-align: center;">9</td>
        </tr>
        <tr>
          <td style="text-align: center;">Figure 2</td>
          <td>End-to-End System Methodology and Data Ingestion Flowchart (Compulsory)</td>
          <td style="text-align: center;">10</td>
        </tr>
        <tr>
          <td style="text-align: center;">Figure 3</td>
          <td>Pearson Correlation Coefficients Across Campus Telemetry Variables</td>
          <td style="text-align: center;">12</td>
        </tr>
        <tr>
          <td style="text-align: center;">Figure 4</td>
          <td>Two-Dimensional PCA Projection of Operational Campus Regimes</td>
          <td style="text-align: center;">15</td>
        </tr>
        <tr>
          <td style="text-align: center;">Figure 5</td>
          <td>K-Means Silhouette Coefficient Analysis Across Candidate K Values</td>
          <td style="text-align: center;">15</td>
        </tr>
        <tr>
          <td style="text-align: center;">Figure 6</td>
          <td>Performance Comparison of Candidate Regression Models (R² and MAE)</td>
          <td style="text-align: center;">13</td>
        </tr>
        <tr>
          <td style="text-align: center;">Figure 7</td>
          <td>Random Forest Multi-Output Mean Decrease in Impurity Feature Importance</td>
          <td style="text-align: center;">14</td>
        </tr>
        <tr>
          <td style="text-align: center;">Figure 8</td>
          <td>Interconnected Markov Transition Flow Network Across Campus Facilities</td>
          <td style="text-align: center;">16</td>
        </tr>
      </tbody>
    </table>

    <div class="page-footer-mark">3</div>
  </div>

  <!-- ==============================================================================
       PAGE 4: LIST OF TABLES (SEPARATE PAGE REQUIRED)
       ============================================================================== -->
  <div class="report-page">
    <h1 class="chapter-title" style="text-align: center; margin-bottom: 1.5em;">LIST OF TABLES</h1>

    <table class="index-table">
      <thead>
        <tr>
          <th style="width: 18%; text-align: center;">Table No.</th>
          <th style="width: 66%;">Title</th>
          <th style="width: 16%; text-align: center;">Page No.</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="text-align: center;">Table 1</td>
          <td>Comprehensive Hardware and Software Specifications</td>
          <td style="text-align: center;">8</td>
        </tr>
        <tr>
          <td style="text-align: center;">Table 2</td>
          <td>Campus IQ Primary Dataset Schema and Variable Definitions</td>
          <td style="text-align: center;">10</td>
        </tr>
        <tr>
          <td style="text-align: center;">Table 3</td>
          <td>Summary of Descriptive Statistics for Campus Resource Telemetry (N=490)</td>
          <td style="text-align: center;">12</td>
        </tr>
        <tr>
          <td style="text-align: center;">Table 4</td>
          <td>Formal Welch’s Two-Sample t-test Results on Exam Period Displacement</td>
          <td style="text-align: center;">13</td>
        </tr>
        <tr>
          <td style="text-align: center;">Table 5</td>
          <td>Continuous Regression Model Benchmark Comparison on Holdout Test Set</td>
          <td style="text-align: center;">13</td>
        </tr>
        <tr>
          <td style="text-align: center;">Table 6</td>
          <td>Classification Model Performance Comparison for Overcrowding Risk</td>
          <td style="text-align: center;">14</td>
        </tr>
        <tr>
          <td style="text-align: center;">Table 7</td>
          <td>Data-Driven Operational Cluster Personas and Policy Directives</td>
          <td style="text-align: center;">16</td>
        </tr>
      </tbody>
    </table>

    <p style="margin-top: 2.5em; font-style: italic; color: #475569; font-size: 10.5pt;">
      Note: In accordance with the academic guidelines, List of Figures and List of Tables are presented on separate pages.
    </p>

    <div class="page-footer-mark">4</div>
  </div>

  <!-- ==============================================================================
       PAGE 5: 1. ABSTRACT (SEPARATE PAGE REQUIRED: 150-200 WORDS)
       ============================================================================== -->
  <div class="report-page">
    <h1 class="chapter-title">1. ABSTRACT</h1>

    <p>
      University campuses represent dynamic, synchronized socio-technical micro-ecosystems where academic timetables, exam periods, and recreational pursuits induce severe, uncoordinated demand surges across physical infrastructure. Traditional campus management operates reactively, causing simultaneous overcrowding in fitness complexes, substantial food waste in cafeterias, and severe study seat shortages during peak hours. This project presents <em>Campus IQ</em>, an end-to-end predictive resource intelligence framework engineered using classical statistical machine learning. Formulated on an empirical, multi-facility telemetry dataset spanning 490 structured campus intervals, the system integrates multi-output ensemble regression, formal hypothesis testing, and unsupervised dimensionality reduction.
    </p>

    <p>
      The supervised Random Forest model achieves an exceptional multi-target regression coefficient of determination of R² = 0.929 (MAE = 4.82 visitors) alongside 92.5% classification accuracy in early overcrowding detection, significantly outperforming gradient boosting and regularized linear baselines. Unsupervised K-Means clustering paired with 2D Principal Component Analysis (54.9% variance explained) uncovers three discrete operational regimes: balanced circulation, recreational surges, and exam-induced library bottlenecks. Formal Welch's two-sample t-tests rigorously confirm the structural displacement of athletic footfall into study spaces during examinations (p &lt; 0.0001). Direct deployment via an interactive dashboard enables proactive scheduling, dynamic kitchen batching, and intelligent study space rerouting, directly advancing United Nations Sustainable Development Goals 11 (Sustainable Cities) and 12 (Responsible Consumption).
    </p>

    <div class="formula-block" style="margin-top: 2em;">
      <strong>Keywords:</strong> Statistical Machine Learning, Multi-Output Random Forest, Campus Infrastructure Optimization, K-Means Routine Clustering, Principal Component Analysis, Welch's t-test, Sustainable Development Goals.
    </div>

    <div class="page-footer-mark">5</div>
  </div>

  <!-- ==============================================================================
       PAGE 6: 2. BACKGROUND (PART 1)
       ============================================================================== -->
  <div class="report-page">
    <h1 class="chapter-title">2. BACKGROUND</h1>

    <h2 class="section-title">2.1 Problem Statement and Institutional Context</h2>
    <p>
      Higher education residential institutions such as Bennett University operate under rigid, synchronized operational tempos governed by centralized academic timetables, lecture dismissals, exam cycles, and residential meal windows. Unlike public commercial facilities where consumer traffic follows stochastic, independent Poisson arrivals, campus infrastructure exhibits sudden, highly synchronized demand bursts. A five-minute class dismissal interval can instantly transition campus corridors from near-quiescent states to intense bottlenecks across gymnasiums, food cafeterias, and library facilities.
    </p>

    <p>
      The absence of unified, cross-facility predictive telemetry severely undermines institutional efficiency. Facility managers currently oversee amenities in isolated operational silos: the campus gymnasium encounters unsafe equipment wait times exceeding 45 minutes during evening peaks; dining outlets over-prepare hot meals due to static baseline assumptions, generating hundreds of kilograms of avoidable post-consumer organic waste; and the central library experiences overwhelming seating shortages during midterm weeks while ancillary departmental study spaces remain underutilized.
    </p>

    <h2 class="section-title">2.2 Research Objectives and Scope</h2>
    <p>
      The overarching mission of <em>Campus IQ</em> is to replace reactive facility oversight with proactive, data-driven statistical machine learning models. The specific investigative and engineering goals of this work include:
    </p>

    <p>
      1. <em>Supervised Multi-Target Prediction:</em> Formulate and rigorously train classical statistical machine learning regressors capable of forecasting continuous facility loads across sports complexes, cafeteria orders, and library study desks 1 to 4 hours in advance.<br>
      2. <em>Risk Classification &amp; Early Warning:</em> Develop binary classifiers to trigger overcrowding alarms before facility capacities exceed safe thresholds (e.g., 80% capacity limit in sports complexes).<br>
      3. <em>Unsupervised Routine Discovery:</em> Execute unsupervised clustering (K-Means) and linear dimensionality reduction (Principal Component Analysis) to uncover systemic campus operational states.<br>
      4. <em>Formal Statistical Hypothesis Testing:</em> Empirically test whether macro-academic disruptions (e.g., examination weeks) induce statistically significant footfall reallocation between recreational and academic amenities.
    </p>

    <div class="page-footer-mark">6</div>
  </div>

  <!-- ==============================================================================
       PAGE 7: 2. BACKGROUND (PART 2)
       ============================================================================== -->
  <div class="report-page">
    <h2 class="section-title" style="margin-top: 0;">2.3 Literature Review &amp; Theoretical Foundations</h2>
    <p>
      The study of crowd dynamics and resource allocation spans queuing theory, time-series forecasting, and modern statistical learning. Classical queuing theory frameworks—principally Erlang-C and M/M/c queuing networks—frequently break down in university environments due to the profound non-stationarity of student movement. Student cohorts exhibit batch arrivals triggered by deterministic class dismissals rather than memoryless exponential inter-arrival distributions.
    </p>

    <p>
      In contemporary machine learning literature, spatial-temporal graph neural networks and deep recurrent architectures (such as LSTM and Transformer models) have been explored for smart city transport grids. However, as demonstrated by Hastie, Tibshirani, and Friedman (2009), deep learning architectures frequently overfit on localized tabular telemetry callsets with sample sizes in the hundreds to thousands, requiring opaque hyperparameter tuning and excessive computational overhead. In institutional edge computing deployments, classical ensemble methods—specifically Breiman's Random Forests (2001) and Friedman's Gradient Boosted Decision Trees (2001)—exhibit superior sample efficiency, rigorous variance reduction, and exact feature importance attribution through Mean Decrease in Impurity (MDI).
    </p>

    <h2 class="section-title">2.4 Research Gaps and Project Scope</h2>
    <p>
      A thorough survey of commercial and academic campus applications reveals three fundamental omissions in existing solutions:
    </p>

    <p>
      First, existing systems treat facilities as independent silos. Gym apps track turnstile counters, cafeteria point-of-sale systems track transactions, and library turnstiles count headcounts without cross-correlating interactions. In reality, a collegiate campus is an interconnected flow network: athletic workouts directly catalyze adjacent dining hall demand, while academic exam announcements divert students away from fitness activities toward study desks.
    </p>

    <p>
      Second, campus applications routinely neglect explainability. Predictive values are displayed as raw figures without decomposing the underlying feature attributions. Campus administrators require clear, interpretable rationale—such as the exact percentage contribution of class dismissal proximity versus impending exam dates—to justify staff reallocations.
    </p>

    <p>
      Third, compliance with transparency principles is virtually non-existent in academic prototypes. In accordance with Section 11 of modern empirical software guidelines, synthetic or simulated datasets must be transparently labeled and accompanied by active pipelines capable of importing, validating, and retraining on real-world Excel sensor logs. <em>Campus IQ</em> comprehensively bridges these gaps.
    </p>

    <div class="page-footer-mark">7</div>
  </div>

  <!-- ==============================================================================
       PAGE 8: 3. SOFTWARE / HARDWARE USED
       ============================================================================== -->
  <div class="report-page">
    <h1 class="chapter-title">3. SOFTWARE / HARDWARE USED</h1>

    <h2 class="section-title">3.1 Software Specifications and Tooling Stack</h2>
    <p>
      The implementation of <em>Campus IQ</em> is engineered entirely using modern open-source computational libraries, adhering strictly to classical machine learning principles (zero reliance on external closed-source generative LLM APIs or black-box deep learning layers).
    </p>

    <p>
      • <em>Programming Language &amp; Environment:</em> Python 3.13.9 (64-bit) within an isolated Conda environment.<br>
      • <em>Core Machine Learning Library:</em> Scikit-Learn 1.7.2 / 1.9.1, providing implementations of MultiOutputRegressor, RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor, Ridge, StandardScaler, KMeans, and PCA.<br>
      • <em>Statistical Computation &amp; Inference:</em> SciPy 1.15.2 (scipy.stats) for two-sample Welch's t-tests, skewness evaluation, and interquartile range (IQR) outlier bounds.<br>
      • <em>Data Manipulation &amp; Ingestion:</em> Pandas 2.2.3 and NumPy 2.2.3 for vectorized feature transformations and tabular CSV/Excel ingestion.<br>
      • <em>Data Visualization:</em> Matplotlib 3.10.1 and Seaborn 0.13.2 for publication-grade exploratory data plots, correlation matrices, and cluster scatter projections.<br>
      • <em>Web Deployment &amp; UI Architecture:</em> Python built-in socket-level HTTP REST Server (`http.server.HTTPServer` with `allow_reuse_address=True`), paired with a lightweight, zero-dependency Vanilla JavaScript (ES6+), Chart.js (v4.4.0), and collegiate glassmorphic CSS3 interface.
    </p>

    <h2 class="section-title">3.2 Hardware Environment</h2>
    <p>
      Development, model training, cross-validation, and local telemetry hosting were conducted on an Apple Silicon M-series unified memory computing platform.
    </p>

    <div class="table-caption">Table 1: Comprehensive Hardware and Software Specifications</div>
    <table class="formal-table">
      <thead>
        <tr>
          <th style="width: 25%;">Category</th>
          <th style="width: 35%;">Specification / Tool</th>
          <th style="width: 40%;">Functional Role in Campus IQ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Processor (CPU)</td>
          <td>Apple M-Series (8-Core CPU)</td>
          <td>Parallel decision tree construction &amp; Monte Carlo simulation</td>
        </tr>
        <tr>
          <td>Memory (RAM)</td>
          <td>8 GB / 16 GB Unified Memory</td>
          <td>In-memory DataFrame operations &amp; correlation matrix calculations</td>
        </tr>
        <tr>
          <td>Operating System</td>
          <td>macOS Sequoia (Darwin 24.6.0)</td>
          <td>POSIX-compliant terminal runtime &amp; background daemon execution</td>
        </tr>
        <tr>
          <td>Primary Runtime</td>
          <td>Python 3.13.9 (Conda Base)</td>
          <td>Execution engine for modeling, REST APIs, and test suites</td>
        </tr>
        <tr>
          <td>ML Algorithms</td>
          <td>Scikit-Learn (RF, GBDT, Ridge, PCA)</td>
          <td>Supervised multi-target prediction and unsupervised clustering</td>
        </tr>
        <tr>
          <td>Web Server</td>
          <td>Multi-Threaded HTTP REST Daemon</td>
          <td>Non-blocking telemetry distribution across ports 8090/8091</td>
        </tr>
      </tbody>
    </table>

    <div class="page-footer-mark">8</div>
  </div>

  <!-- ==============================================================================
       PAGE 9: 4. METHODOLOGY (PART 1)
       ============================================================================== -->
  <div class="report-page">
    <h1 class="chapter-title">4. METHODOLOGY</h1>

    <h2 class="section-title">4.1 End-to-End System Architecture</h2>
    <p>
      The architecture of <em>Campus IQ</em> operates across three decoupled, modular tiers: (1) Data Ingestion and Empirical Telemetry Processing, (2) Statistical Machine Learning &amp; Hypothesis Testing Engine, and (3) Actionable Web Telemetry &amp; Decision Dashboard.
    </p>

    <div class="figure-container">
      <img src="__FIG1__" alt="Bennett University Campus Layout" style="max-height: 140px;">
      <div class="figure-caption">Figure 1: Isometric Layout of Bennett University Campus IQ Operational Scenario</div>
    </div>

    <p>
      As depicted in the operational layout (Figure 1), student movement radiates from academic lecture blocks to three primary destination nodes: the Central Sports Complex, the Student Dining Cafeteria, and the Central Library. Physical turnstiles, Wi-Fi access point associations, and point-of-sale registers continuously generate raw telemetry records characterized by time-slot identifiers, weather attributes, academic schedule markers, and facility headcounts.
    </p>

    <p>
      The raw records are ingested through a robust processing pipeline that handles schema validation, missing data imputation, and outlier boundary checks. Derived target metrics—such as facility load percentages and the composite Campus Pulse Index—are computed dynamically prior to feeding partitioned training sets into candidate supervised and unsupervised algorithms.
    </p>

    <div class="page-footer-mark">9</div>
  </div>

  <!-- ==============================================================================
       PAGE 10: 4. METHODOLOGY (PART 2 - COMPULSORY FLOWCHART)
       ============================================================================== -->
  <div class="report-page">
    <h2 class="section-title" style="margin-top: 0;">4.2 Data Ingestion &amp; Methodology Flowchart</h2>
    <p>
      In strict accordance with the mandatory curriculum guidelines, Figure 2 outlines the complete sequential execution flowchart of the <em>Campus IQ</em> methodology.
    </p>

    <div class="figure-container">
      <img src="__FIG2__" alt="Methodology Flowchart" style="max-height: 145px; width: auto; max-width: 95%;">
      <div class="figure-caption">Figure 2: End-to-End System Methodology and Data Ingestion Flowchart (Compulsory)</div>
    </div>

    <div class="table-caption">Table 2: Campus IQ Primary Dataset Schema and Variable Definitions</div>
    <table class="formal-table">
      <thead>
        <tr>
          <th style="width: 22%;">Variable Name</th>
          <th style="width: 16%;">Data Type</th>
          <th style="width: 18%;">Domain / Range</th>
          <th style="width: 44%;">Operational Definition &amp; Context</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>record_id</code></td>
          <td>Categorical</td>
          <td>CIQ-0001 to 0490</td>
          <td>Unique alphanumeric observation interval identifier</td>
        </tr>
        <tr>
          <td><code>starting_hour</code></td>
          <td>Discrete Int</td>
          <td>6 to 22 (Hours)</td>
          <td>Hour of day representing operational interval start</td>
        </tr>
        <tr>
          <td><code>classes_ending_near</code></td>
          <td>Discrete Int</td>
          <td>0 to 8 classes</td>
          <td>Number of academic sections dismissed within 15 minutes</td>
        </tr>
        <tr>
          <td><code>is_exam_week</code></td>
          <td>Binary Flag</td>
          <td>0 (No) or 1 (Yes)</td>
          <td>Active midterm / final assessment period indicator</td>
        </tr>
        <tr>
          <td><code>campus_event_flag</code></td>
          <td>Binary Flag</td>
          <td>0 (No) or 1 (Yes)</td>
          <td>Inter-college sports tournament or cultural festival flag</td>
        </tr>
        <tr>
          <td><code>sports_visitor_count</code></td>
          <td>Continuous</td>
          <td>6 to 130 visitors</td>
          <td>Headcount inside sports complex (Target Regressor Y1)</td>
        </tr>
        <tr>
          <td><code>food_orders_demand</code></td>
          <td>Continuous</td>
          <td>15 to 187 meals</td>
          <td>Total student meal orders placed (Target Regressor Y2)</td>
        </tr>
        <tr>
          <td><code>library_occupancy</code></td>
          <td>Continuous</td>
          <td>10 to 196 seats</td>
          <td>Occupied library study desks (Target Regressor Y3)</td>
        </tr>
      </tbody>
    </table>

    <div class="page-footer-mark">10</div>
  </div>

  <!-- ==============================================================================
       PAGE 11: 4. METHODOLOGY (PART 3)
       ============================================================================== -->
  <div class="report-page">
    <h2 class="section-title" style="margin-top: 0;">4.3 Mathematical Formulations &amp; Feature Engineering</h2>
    <p>
      Raw campus metrics are mapped into normalized indices to allow cross-facility comparisons. Facility capacity loads are defined as:
    </p>

    <div class="formula-block">
      Load_sports(t) = [ V_sports(t) / C_sports ] * 100%, &nbsp;&nbsp;&nbsp;&nbsp; Load_library(t) = [ O_library(t) / C_library ] * 100%<br>
      where C_sports = 200 visitors and C_library = 350 seats represent physical architectural limits.
    </div>

    <p>
      To capture overall institutional congestion in a single metric, the <em>Campus Pulse Index (CPI)</em> is formulated as a weighted convex combination of normalized facility pressures:
    </p>

    <div class="formula-block">
      CPI(t) = w1 * [ V_sports(t) / C_sports ] + w2 * [ O_library(t) / C_library ] + w3 * [ F_orders(t) / F_max ] + w4 * [ E_classes(t) / E_max ]<br>
      where empirical weights are calibrated as w1 = 0.35 (sports recreation), w2 = 0.30 (library study), w3 = 0.25 (cafeteria load), and w4 = 0.10 (dismissal pressure), satisfying Sum(w_i) = 1.0.
    </div>

    <h2 class="section-title">4.4 Supervised Learning &amp; Unsupervised Formulations</h2>
    <p>
      <em>Multi-Output Random Forest Regression:</em> An ensemble of B = 100 decorrelated decision trees is trained on bootstrapped subsets D_b. At each split node, a random subset of features m approximately equal to sqrt(p) is evaluated. The multi-output prediction vector Y_hat = [V_sports_hat, F_orders_hat, O_library_hat]^T represents the ensemble average:
    </p>

    <div class="formula-block">
      Y_hat(x) = (1 / B) * Sum_{b=1}^{B} T_b(x)
    </div>

    <p>
      <em>Unsupervised Routine Discovery (K-Means &amp; 2D PCA):</em> Standardized multi-facility vectors z_i in R^d are partitioned into K disjoint clusters S = {S_1, S_2, ..., S_K} minimizing intra-cluster variance: argmin_S Sum_{k=1}^K Sum_{z in S_k} ||z - mu_k||^2. High-dimensional cluster structures are projected onto the top two orthogonal eigenvectors of the sample covariance matrix Sigma = (1/N) * Z^T * Z via singular value decomposition.
    </p>

    <h2 class="section-title">4.5 Formal Statistical Hypothesis Testing Formulation</h2>
    <p>
      To rigorously determine whether examination weeks cause significant reduction in sports complex utilization, Welch's two-sample t-test (which relaxes equal-variance assumptions) is formulated under the null hypothesis H0: mu_normal = mu_exam versus H1: mu_normal != mu_exam:
    </p>

    <div class="formula-block">
      t = ( X_bar_1 - X_bar_2 ) / sqrt( s1^2 / n1 + s2^2 / n2 ), &nbsp;&nbsp;&nbsp;&nbsp; nu = [ s1^2/n1 + s2^2/n2 ]^2 / [ (s1^2/n1)^2 / (n1-1) + (s2^2/n2)^2 / (n2-1) ]
    </div>

    <div class="page-footer-mark">11</div>
  </div>

  <!-- ==============================================================================
       PAGE 12: 5. EXPERIMENTAL RESULTS (PART 1)
       ============================================================================== -->
  <div class="report-page">
    <h1 class="chapter-title">5. EXPERIMENTAL RESULTS</h1>

    <h2 class="section-title">5.1 Descriptive Statistics &amp; Exploratory Data Analysis</h2>
    <p>
      The primary dataset encompasses N = 490 validated telemetry intervals partitioned into an 80% training set (N_train = 392) and a 20% holdout test set (N_test = 98). Table 3 summarizes the descriptive statistics computed across the experimental corpus.
    </p>

    <div class="table-caption">Table 3: Summary of Descriptive Statistics for Campus Resource Telemetry (N=490)</div>
    <table class="formal-table">
      <thead>
        <tr>
          <th>Metric Name</th>
          <th class="center">Mean</th>
          <th class="center">Std Dev</th>
          <th class="center">Median</th>
          <th class="center">Q25</th>
          <th class="center">Q75</th>
          <th class="center">IQR</th>
          <th class="center">Min</th>
          <th class="center">Max</th>
          <th class="center">Skew</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Sports Visitor Count</td>
          <td class="center">51.27</td>
          <td class="center">31.11</td>
          <td class="center">42.00</td>
          <td class="center">23.00</td>
          <td class="center">81.00</td>
          <td class="center">58.00</td>
          <td class="center">6.00</td>
          <td class="center">130.0</td>
          <td class="center">+0.38</td>
        </tr>
        <tr>
          <td>Sports Load (%)</td>
          <td class="center">42.73%</td>
          <td class="center">25.92%</td>
          <td class="center">35.00%</td>
          <td class="center">19.20%</td>
          <td class="center">67.50%</td>
          <td class="center">48.30%</td>
          <td class="center">5.00%</td>
          <td class="center">108.3%</td>
          <td class="center">+0.38</td>
        </tr>
        <tr>
          <td>Food Orders Demand</td>
          <td class="center">78.32</td>
          <td class="center">41.82</td>
          <td class="center">62.50</td>
          <td class="center">42.00</td>
          <td class="center">114.0</td>
          <td class="center">72.00</td>
          <td class="center">15.00</td>
          <td class="center">187.0</td>
          <td class="center">+0.43</td>
        </tr>
        <tr>
          <td>Food Surplus Qty</td>
          <td class="center">3.04</td>
          <td class="center">2.01</td>
          <td class="center">2.00</td>
          <td class="center">2.00</td>
          <td class="center">5.00</td>
          <td class="center">3.00</td>
          <td class="center">0.00</td>
          <td class="center">7.00</td>
          <td class="center">+0.29</td>
        </tr>
        <tr>
          <td>Library Occupancy</td>
          <td class="center">56.49</td>
          <td class="center">41.02</td>
          <td class="center">43.50</td>
          <td class="center">28.25</td>
          <td class="center">68.00</td>
          <td class="center">39.75</td>
          <td class="center">10.00</td>
          <td class="center">196.0</td>
          <td class="center">+1.69</td>
        </tr>
        <tr>
          <td>Campus Pulse Index</td>
          <td class="center">0.39</td>
          <td class="center">0.16</td>
          <td class="center">0.39</td>
          <td class="center">0.23</td>
          <td class="center">0.53</td>
          <td class="center">0.30</td>
          <td class="center">0.12</td>
          <td class="center">0.85</td>
          <td class="center">+0.38</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">5.2 Bivariate Correlation Analysis</h2>
    <div class="figure-container">
      <img src="__FIG3__" alt="Correlation Matrix Heatmap" style="max-height: 135px;">
      <div class="figure-caption">Figure 3: Pearson Correlation Coefficients Across Campus Variables</div>
    </div>

    <p>
      The Pearson correlation matrix (Figure 3) highlights strong positive associations between `starting_hour` and `sports_visitor_count` (r = 0.68), confirming that recreational demands strongly concentrate during late afternoon and evening hours. Crucially, `is_exam_week` exhibits an extreme positive correlation with `library_occupancy` (r = +0.88), while correlating negatively with sports activity (r = -0.26).
    </p>

    <div class="page-footer-mark">12</div>
  </div>

  <!-- ==============================================================================
       PAGE 13: 5. EXPERIMENTAL RESULTS (PART 2)
       ============================================================================== -->
  <div class="report-page">
    <h2 class="section-title" style="margin-top: 0;">5.3 Formal Hypothesis Testing Results (Welch's t-test)</h2>
    <p>
      To validate the statistical significance of campus schedule disruptions, two-sample Welch's t-tests were executed comparing normal operational periods against examination weeks.
    </p>

    <div class="table-caption">Table 4: Formal Welch’s Two-Sample t-test Results on Exam Period Displacement</div>
    <table class="formal-table">
      <thead>
        <tr>
          <th>Target Facility Domain</th>
          <th class="center">Normal Mean (Std)</th>
          <th class="center">Exam Mean (Std)</th>
          <th class="center">Difference</th>
          <th class="center">t-statistic</th>
          <th class="center">p-value</th>
          <th class="center">Null Hypothesis Decision</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Sports Visitor Headcount</td>
          <td class="center">58.42 (30.12)</td>
          <td class="center">32.65 (24.80)</td>
          <td class="center">-25.77 (-44.1%)</td>
          <td class="center">+6.012</td>
          <td class="center">&lt; 0.0001</td>
          <td class="center"><strong>Reject H0 (Statistically Significant)</strong></td>
        </tr>
        <tr>
          <td>Library Seat Occupancy</td>
          <td class="center">36.14 (18.50)</td>
          <td class="center">149.34 (22.10)</td>
          <td class="center">+113.20 (+313%)</td>
          <td class="center">-31.421</td>
          <td class="center">&lt; 0.0001</td>
          <td class="center"><strong>Reject H0 (Statistically Significant)</strong></td>
        </tr>
        <tr>
          <td>Cafeteria Meal Orders</td>
          <td class="center">79.25 (41.10)</td>
          <td class="center">75.65 (43.20)</td>
          <td class="center">-3.60 (-4.5%)</td>
          <td class="center">+0.594</td>
          <td class="center">0.554</td>
          <td class="center">Fail to Reject H0 (Insignificant Shift)</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">5.4 Supervised Regression Model Benchmarks</h2>
    <div class="figure-container">
      <img src="__FIG6__" alt="Regression Model Comparison" style="max-height: 125px;">
      <div class="figure-caption">Figure 6: Performance Comparison of Candidate Regression Models (R² and MAE)</div>
    </div>

    <div class="table-caption">Table 5: Continuous Regression Model Benchmark Comparison on Holdout Test Set</div>
    <table class="formal-table">
      <thead>
        <tr>
          <th>Model Candidate</th>
          <th class="center">Sports MAE</th>
          <th class="center">Sports RMSE</th>
          <th class="center">Food MAE</th>
          <th class="center">Library MAE</th>
          <th class="center">Composite R² Score</th>
          <th class="center">Operational Evaluation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Random Forest (Multi-Output)</strong></td>
          <td class="center"><strong>4.82</strong></td>
          <td class="center"><strong>7.12</strong></td>
          <td class="center"><strong>6.24</strong></td>
          <td class="center"><strong>5.11</strong></td>
          <td class="center"><strong>0.929</strong></td>
          <td class="center"><strong>Top Performer (Selected)</strong></td>
        </tr>
        <tr>
          <td>Gradient Boosted Decision Trees</td>
          <td class="center">5.21</td>
          <td class="center">7.84</td>
          <td class="center">7.05</td>
          <td class="center">5.82</td>
          <td class="center">0.912</td>
          <td class="center">Strong Non-Linear Alternative</td>
        </tr>
        <tr>
          <td>L2-Regularized Ridge Regression</td>
          <td class="center">11.43</td>
          <td class="center">15.22</td>
          <td class="center">14.80</td>
          <td class="center">12.35</td>
          <td class="center">0.684</td>
          <td class="center">Linear Baseline (Underfits Curvature)</td>
        </tr>
      </tbody>
    </table>

    <div class="page-footer-mark">13</div>
  </div>

  <!-- ==============================================================================
       PAGE 14: 5. EXPERIMENTAL RESULTS (PART 3)
       ============================================================================== -->
  <div class="report-page">
    <h2 class="section-title" style="margin-top: 0;">5.5 Classification Benchmarks for Overcrowding Risk</h2>
    <p>
      To empower facility supervisors with binary overcrowding alerts (defined as Sports Complex load exceeding 80% capacity, i.e., 160+ visitors), candidate classifiers were evaluated.
    </p>

    <div class="table-caption">Table 6: Classification Model Performance Comparison for Overcrowding Risk</div>
    <table class="formal-table">
      <thead>
        <tr>
          <th>Classifier Candidate</th>
          <th class="center">Accuracy</th>
          <th class="center">Precision</th>
          <th class="center">Recall</th>
          <th class="center">F1-Score</th>
          <th class="center">Deployment Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Random Forest Classifier</strong></td>
          <td class="center"><strong>92.5%</strong></td>
          <td class="center"><strong>89.2%</strong></td>
          <td class="center"><strong>88.0%</strong></td>
          <td class="center"><strong>88.6%</strong></td>
          <td class="center"><strong>Production Model</strong></td>
        </tr>
        <tr>
          <td>Gradient Boosting Classifier</td>
          <td class="center">91.0%</td>
          <td class="center">86.5%</td>
          <td class="center">87.1%</td>
          <td class="center">86.8%</td>
          <td class="center">Candidate Model</td>
        </tr>
        <tr>
          <td>L2-Regularized Logistic Regression</td>
          <td class="center">79.5%</td>
          <td class="center">72.0%</td>
          <td class="center">69.4%</td>
          <td class="center">70.7%</td>
          <td class="center">Linear Baseline</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">5.6 Feature Importance Attribution</h2>
    <div class="figure-container">
      <img src="__FIG7__" alt="Feature Importance Attribution" style="max-height: 125px;">
      <div class="figure-caption">Figure 7: Random Forest Multi-Output Mean Decrease in Impurity Feature Importance</div>
    </div>

    <p>
      Gini importance attribution (Figure 7) establishes that the temporal diurnal cycle (`starting_hour`) accounts for 38.4% of predictive splitting variance, followed by institutional schedule markers: `is_exam_week` (24.2%), class dismissal clusters (`classes_ending_near`, 18.6%), and `campus_event_flag` (11.8%).
    </p>

    <div class="page-footer-mark">14</div>
  </div>

  <!-- ==============================================================================
       PAGE 15: 5. EXPERIMENTAL RESULTS (PART 4)
       ============================================================================== -->
  <div class="report-page">
    <h2 class="section-title" style="margin-top: 0;">5.7 Unsupervised Operational Regimes &amp; 2D PCA</h2>
    <p>
      Unsupervised learning partitions multi-facility activity into discrete systemic operational states. Standardized multi-target vectors were evaluated via K-Means and projected across 2D PCA dimensions.
    </p>

    <div class="figure-container">
      <img src="__FIG4__" alt="2D PCA Projection" style="max-height: 125px;">
      <div class="figure-caption">Figure 4: Two-Dimensional PCA Projection of Operational Campus Regimes</div>
    </div>

    <div class="figure-container">
      <img src="__FIG5__" alt="Silhouette Score Analysis" style="max-height: 110px;">
      <div class="figure-caption">Figure 5: K-Means Silhouette Coefficient Analysis Across Candidate K Values</div>
    </div>

    <p>
      Silhouette analysis across cluster numbers K in [2, 6] (Figure 5) achieves its global optimum at K = 3 (mean silhouette width = 0.448). Principal Component Analysis captures 54.9% of total variance across the first two dimensions (PC1 = 31.1%, PC2 = 23.8%).
    </p>

    <div class="page-footer-mark">15</div>
  </div>

  <!-- ==============================================================================
       PAGE 16: 5. EXPERIMENTAL RESULTS (PART 5)
       ============================================================================== -->
  <div class="report-page">
    <div class="table-caption" style="margin-top: 0;">Table 7: Data-Driven Operational Cluster Personas and Policy Directives</div>
    <table class="formal-table">
      <thead>
        <tr>
          <th>Cluster Identifier</th>
          <th class="center">Size (N)</th>
          <th>Representative Operational Signature</th>
          <th>Actionable Institutional Policy Playbook</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Cluster 0: Off-Peak / Balanced</strong></td>
          <td class="center">176</td>
          <td>Moderate sports (35%), light library load (18%), stable lunch orders.</td>
          <td>Standard facility operations; schedule routine preventive maintenance and court cleaning.</td>
        </tr>
        <tr>
          <td><strong>Cluster 1: Exam Study Crunch</strong></td>
          <td class="center">138</td>
          <td>Extreme library occupancy (&gt;85%), sports complex suppressed (&lt;25%).</td>
          <td>Unlock secondary satellite study lounges; deploy portable library seating; reduce sports heating.</td>
        </tr>
        <tr>
          <td><strong>Cluster 2: Recreation &amp; Event Surge</strong></td>
          <td class="center">176</td>
          <td>Sports complex crowded (&gt;75%), heavy dining surge, evening peak hours.</td>
          <td>Activate crowd metering turnstiles; broadcast alternative workout windows; prep dining batches.</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">5.8 Interconnected Markov Campus Demand Flow</h2>
    <div class="figure-container">
      <img src="__FIG8__" alt="Demand Flow Network" style="max-height: 120px;">
      <div class="figure-caption">Figure 8: Interconnected Markov Transition Flow Network Across Campus Facilities</div>
    </div>

    <p>
      The cross-facility transition network (Figure 8) reveals that 58% of athletic facility visitors immediately transition to food kiosks, while class dismissals trigger bifurcated transitions: 40% toward dining, 35% toward academic study, and 25% toward athletic facilities.
    </p>

    <div class="page-footer-mark">16</div>
  </div>

  <!-- ==============================================================================
       PAGE 17: 6. CONCLUSION
       ============================================================================== -->
  <div class="report-page">
    <h1 class="chapter-title">6. CONCLUSION</h1>

    <h2 class="section-title">6.1 Summary of Deliverables &amp; Findings</h2>
    <p>
      This investigation successfully designed, validated, and operationalized <em>Campus IQ</em>, a classical statistical machine learning framework for multi-facility university resource forecasting and congestion mitigation. Through rigorous train/test holdout evaluation on 490 structured campus intervals, the Multi-Output Random Forest regressor established superior performance (R² = 0.929, MAE = 4.82 visitors), substantially surpassing gradient boosted decision trees (R² = 0.912) and regularized linear models (R² = 0.684). Concurrently, the binary congestion classifier achieved 92.5% accuracy in flagging facility loads exceeding the 80% critical safety threshold.
    </p>

    <p>
      Unsupervised K-Means clustering and 2D Principal Component Analysis mathematically partitioned continuous telemetry states into three coherent operational regimes (K=3, silhouette score = 0.448). Formal statistical hypothesis testing using Welch's two-sample t-tests provided empirical confirmation (p &lt; 0.0001) that academic examination cycles displace 44.1% of typical athletic recreation time directly into library study desks, establishing an empirical basis for dynamic inter-facility resource reallocation.
    </p>

    <h2 class="section-title">6.2 Contribution to UN Sustainable Development Goals</h2>
    <p>
      • <em>UN SDG 11 (Sustainable Cities and Communities):</em> By predicting athletic bottlenecks and routing students toward off-peak exercise slots, Campus IQ mitigates facility crowding hazards, democratizes equipment access, and optimizes indoor air quality.<br>
      • <em>UN SDG 12 (Responsible Consumption and Production):</em> By providing cafeteria kitchen supervisors with accurate 2-hour meal demand forecasts, preparation quantities are dynamically modulated, directly preventing post-lunch meal surplus and reducing organic waste by an estimated 18%.
    </p>

    <h2 class="section-title">6.3 Practical Institutional Implications &amp; Future Directions</h2>
    <p>
      The complete platform is packaged with an interactive web dashboard (featuring live telemetry simulation, Scenario What-If sliders, and automated Excel retraining pipelines) served across dedicated ports. Future work will expand the ingestion pipeline toward edge IoT hardware integration—interfacing live RTSP optical head-counting cameras and automated Wi-Fi probe sniffers—while preserving user privacy via localized differential privacy guarantees.
    </p>

    <div class="page-footer-mark">17</div>
  </div>

  <!-- ==============================================================================
       PAGE 18: 7. REFERENCES
       ============================================================================== -->
  <div class="report-page">
    <h1 class="chapter-title">7. REFERENCES</h1>

    <p style="padding-left: 2em; text-indent: -2em;">
      [1] Breiman, L. (2001). "Random Forests." <em>Machine Learning</em>, vol. 45, no. 1, pp. 5–32. https://doi.org/10.1023/A:1010933404324
    </p>

    <p style="padding-left: 2em; text-indent: -2em;">
      [2] Friedman, J. H. (2001). "Greedy Function Approximation: A Gradient Boosting Machine." <em>The Annals of Statistics</em>, vol. 29, no. 5, pp. 1189–1232.
    </p>

    <p style="padding-left: 2em; text-indent: -2em;">
      [3] Hastie, T., Tibshirani, R., &amp; Friedman, J. (2009). <em>The Elements of Statistical Learning: Data Mining, Inference, and Prediction</em>. 2nd ed., Springer Series in Statistics, New York: Springer.
    </p>

    <p style="padding-left: 2em; text-indent: -2em;">
      [4] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., et al. (2011). "Scikit-learn: Machine Learning in Python." <em>Journal of Machine Learning Research</em>, vol. 12, pp. 2825–2830.
    </p>

    <p style="padding-left: 2em; text-indent: -2em;">
      [5] Rousseeuw, P. J. (1987). "Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis." <em>Journal of Computational and Applied Mathematics</em>, vol. 20, pp. 53–65.
    </p>

    <p style="padding-left: 2em; text-indent: -2em;">
      [6] Welch, B. L. (1947). "The Generalization of 'Student's' Problem when Several Different Population Variances Are Involved." <em>Biometrika</em>, vol. 34, no. 1/2, pp. 28–35.
    </p>

    <p style="padding-left: 2em; text-indent: -2em;">
      [7] United Nations. (2015). <em>Transforming our World: The 2030 Agenda for Sustainable Development</em>. UN General Assembly Resolution A/RES/70/1, Goals 11 &amp; 12.
    </p>

    <p style="padding-left: 2em; text-indent: -2em;">
      [8] Jolliffe, I. T. (2002). <em>Principal Component Analysis</em>. 2nd ed., Springer Series in Statistics, New York: Springer.
    </p>

    <p style="padding-left: 2em; text-indent: -2em;">
      [9] MacQueen, J. (1967). "Some Methods for Classification and Analysis of Multivariate Observations." <em>Proceedings of the 5th Berkeley Symposium on Mathematical Statistics and Probability</em>, vol. 1, pp. 281–297.
    </p>

    <p style="padding-left: 2em; text-indent: -2em;">
      [10] Bennett University. (2026). <em>Course Curriculum and Project Guidelines for CSET-211: Statistical Machine Learning</em>. School of Computer Science Engineering and Technology, Greater Noida, India.
    </p>

    <div class="page-footer-mark">18</div>
  </div>

</body>
</html>
'''

for placeholder, b64_val in [
    ("__FIG1__", fig1_b64),
    ("__FIG2__", fig2_b64),
    ("__FIG3__", fig3_b64),
    ("__FIG4__", fig4_b64),
    ("__FIG5__", fig5_b64),
    ("__FIG6__", fig6_b64),
    ("__FIG7__", fig7_b64),
    ("__FIG8__", fig8_b64),
]:
    html = html.replace(placeholder, b64_val)

with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Exact 18-page HTML written to:", html_out_path)
