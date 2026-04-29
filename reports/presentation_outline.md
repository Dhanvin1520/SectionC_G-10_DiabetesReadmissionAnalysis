# Diabetes 30-Day Readmission Analysis
**A Decision Support Framework for Hospital Management**

---

## Slide 1 — Title Slide
- **Project Title:** Analyzing Clinical & Demographic Patterns to Reduce 30-Day Hospital Readmissions
- **Sector Name:** Healthcare / Health Informatics
- **Team ID:** G-10 (Section C)
- **Team Members:** Dhanvin Vadlamudi (Lead), Ayush Mittal, Gargi Srivastava, Tanish Garg, Sumit Yadav, Lakshya
- **Faculty Mentor Name:** Archit Raj
- **GitHub Repository URL:** https://github.com/Dhanvin1520/SectionC_G-10_DiabetesReadmissionAnalysis
- **Tableau Public Dashboard URL:** https://public.tableau.com/app/profile/ayush.mittal4873/viz/DVACapstoneDiabetesReadmissionAnalysis_v2025_3/Dashboard_Executive_Overview?publish=yes

---

## Slide 2 — Context & Problem Statement
- **Sector Context:** Unplanned 30-day hospital readmissions are a massive operational and financial burden, triggering multi-million dollar penalties under the Hospital Readmissions Reduction Program (HRRP).
- **Decision-Maker:** Chief Medical Officer (CMO) & Discharge Planning Managers.
- **Problem Statement:** How can clinical history, medication patterns, and demographic indicators accurately predict 30-day readmission risk in diabetic patients?
- **Objective:** To transition from "generic discharge protocols" to a "risk-stratified discharge" approach, reducing clinical errors and lowering regulatory penalties.

---

## Slide 3 — Data Engineering (Source to Pipeline)
- **Source:** "Diabetes 130-US Hospitals Dataset" (101,763 rows x 54 columns, spanning 10 years).
- **Python ETL Core Steps:**
  1. Handled widespread "?" missing values and dropped noisy columns (e.g., Weight).
  2. Mapped over 700+ technical ICD-9 codes into 17 high-level clinical groups (e.g., Circulatory, Respiratory).
  3. Capped medication outliers at the 99th percentile to prevent skewing LOS metrics.
- **GitHub Status:** Verified! Notebooks `01_extraction.ipynb` and `02_cleaning.ipynb` are committed.
- **Data Dictionary:** Reference `docs/data_dictionary.md` for metrics like `Prior Inpatient Visits` and `readmitted_under_30`.

---

## Slide 4 — KPI & Metrics Framework
- **Primary KPI:** 30-Day Readmission Rate (%)
  - *Link to Problem:* Directly measures discharge failure and HRRP penalty risk.
- **Secondary KPI:** Average Length of Stay (LOS)
  - *Link to Problem:* Measures bed efficiency; shorter stays may increase readmission risk if premature.
- **Tertiary KPI:** Medication Change Rate (%)
  - *Link to Problem:* Acts as a proxy for clinical instability during the encounter.
- **Computation:** KPIs calculated via Python Pandas `.groupby().mean()` aggregations in `03_eda.ipynb`.

---

## Slide 5 — Key Insights (EDA)
- **Insight 1: The "Frequent Flyer" Danger.** Patients with 3+ prior inpatient visits in the last year return at a 4.5x higher rate than the baseline average.
- **Insight 2: The Age Paradox.** While the 75-85 bracket has the highest raw volume, the 25-35 age group shows a severe secondary "risk peak", highlighting failures in outpatient support for young Type-1 diabetics.
- **Insight 3: Emergency Baseline.** Emergency admissions (53% of volume) carry a higher intrinsic readmission risk than elective surgeries.
- **Insight 4: The Danger of "Long Stays".** Readmission risk steadily increases the longer a patient stays (peaking at 10 days), indicating that long stays reflect high underlying severity.
- **Insight 5: Diagnosis Drivers.** Circulatory conditions account for 30% of all early returns, representing the highest-risk clinical cluster.
- **Insight 6: Testing Gaps.** Patients discharged without an A1C test exhibit a significantly higher readmission rate than those tested.
- **Reference:** Visualized via Matplotlib/Seaborn in `03_eda.ipynb`.

---

## Slide 6 — Advanced Analysis
- **Advanced Method:** Statistical Hypothesis Testing (Mann-Whitney U Test) & Random Forest Feature Importance.
- **New Understanding:** Confirmed statistically ($P < 0.0001$) that a patient's historical visit count is a vastly superior predictor of readmission than their current demographic factors.
- **Feature Ranking:** The classifier identified "Prior Inpatient Visits" and "Number of Lab Procedures" as the top two clinical risk markers.
- **Libraries Used:** `scipy.stats` for significance testing and `sklearn.ensemble` for feature importance mapping (`04_statistical_analysis.ipynb`).

---

## Slide 7 — Tableau Dashboard Walkthrough
- **Executive View:** High-level operational metrics (Refer to `tableau/screenshots/dashboard-1.png`).
- **Operational View:** Patient Risk Analysis (Refer to `tableau/screenshots/dashboard-2.png`).
- **Treatment View:** Impact of Medication & Insulin Titration (Refer to `tableau/screenshots/dashboard-3.png`).
- **Interactive Element to Show:** Click on the "Circulatory" diagnosis box in the Treemap to instantly filter the related discharge disposition charts and see where these patients are going.
- **Dashboard URL:** [View Live on Tableau Public](https://public.tableau.com/app/profile/ayush.mittal4873/viz/DVACapstoneDiabetesReadmissionAnalysis_v2025_3/Dashboard_Executive_Overview?publish=yes)

---

## Slide 8 — Recommendations
1. **Targeted Follow-ups (Nursing):** 
   - *Insight:* $\ge3$ prior visits leads to a 50% readmission rate. 
   - *Recommendation:* Implement an automated 48-hour nurse callback.
   - *Timeline:* 30 Days | Owner: Nursing Staff
2. **Clinical Protocol Shift (Quality):** 
   - *Insight:* Circulatory comorbidities drive 30% of early returns.
   - *Recommendation:* Mandate a "Heart-Diabetes" discharge checklist for these patients.
   - *Timeline:* 60 Days | Owner: Clinical Quality Team
3. **Medication Stability Rules (CMO):** 
   - *Insight:* Decreasing insulin dosages strongly predicts readmission.
   - *Recommendation:* Require attending physician sign-off if insulin is adjusted within 24h of discharge.
   - *Timeline:* Immediate | Owner: Chief Medical Officer
4. **Diagnostic Compliance (Lab):**
   - *Insight:* Patients with "A1C Not Tested" have significantly higher risk.
   - *Recommendation:* Flag these patients for a point-of-care test before discharge.
   - *Timeline:* 15 Days | Owner: Lab Operations

---

## Slide 9 — Impact & Value
- **Cost Savings:** Reducing the 30-day readmission rate by just 5% would avoid an estimated **$1.2M annually** in HRRP penalties.
- **Operational Efficiency:** Preventing these returns frees up an estimated **~2,000 bed-days** per year, allowing the hospital to accommodate higher-margin elective surgeries.
- **Cost of Inaction:** Maintaining the current 11.16% rate ensures ongoing margin compression and degrades hospital quality ratings.

---

## Slide 10 — Limitations & Next Steps
- **Limitations:** The dataset lacks crucial Social Determinants of Health (SDOH) like income and ZIP code, which heavily influence readmission. We also lack out-of-hospital mortality data.
- **Strengthening Findings:** Integrating real-time EMR text notes (using NLP) would capture the nuances of patient compliance and discharge instructions.
- **Next Steps:** Deploy a real-time **Predictive Machine Learning Model (XGBoost)** via an API to flag high-risk patients at the exact moment of admission, moving from retrospective reporting to proactive prevention.

---

## Slide 11 — Team & Contribution
- **Dhanvin Vadlamudi (Lead):** Project strategy, KPI framework, and business logic implementation.
- **Ayush Mittal (Viz Architect):** Tableau architecture, dashboard design, and interactive storytelling.
- **Gargi Srivastava (Data Engineer):** ETL pipeline development, missing value treatment, and feature engineering.
- **Tanish Garg (Stat Lead):** Hypothesis testing (Mann-Whitney), Random Forest modeling, and validation.
- **Sumit Yadav (EDA Lead):** Exploratory trend analysis, patient segmentation, and distribution analysis.
- **Lakshya (QA & Documentation):** LaTeX report development, data dictionary, and quality assurance.
- *All claims verified via GitHub Insights and Pull Request history.*
