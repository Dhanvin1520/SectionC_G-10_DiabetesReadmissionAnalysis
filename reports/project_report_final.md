# 🏥 Diabetes 30-Day Readmission Risk Analysis
**Section C, Group G-10**

---

## 1. Cover Page
*   **Project Title**: Analyzing Clinical & Demographic Patterns to Reduce 30-Day Hospital Readmissions
*   **Sector**: Healthcare / Health Informatics
*   **Team ID**: G-10 (Section C)
*   **Team Members**:
    *   **Dhanvin** (Team Lead | Python ETL & Analysis Pipeline)
    *   **Tanish Garg** (Tableau Dashboard Development)
    *   **Ayush** (Tableau Dashboard Development)
    *   **Sumit** (Report Documentation & Presentation)
    *   **Lakshay** (Report Documentation & Presentation)
*   **Faculty Mentor**: [Mentor Name]
*   **Institute**: Newton School of Technology
*   **GitHub Repository URL**: [https://github.com/Dhanvin1520/SectionC_G-10_DiabetesReadmissionAnalysis](https://github.com/Dhanvin1520/SectionC_G-10_DiabetesReadmissionAnalysis)
*   **Tableau Public Dashboard URL**: [View Dashboard](https://public.tableau.com/app/profile/tanish.garg1945/viz/DVACapstoneDiabetesReadmissionAnalysis/Dashboard_Patient_Risk_Analysis?publish=yes)
*   **Submission Date**: April 28, 2026

---

## 2. Executive Summary
**Problem**: Hospital readmissions for diabetic patients are a major driver of healthcare costs and poor patient outcomes. Reducing the 30-day readmission rate is critical for hospital operational efficiency and regulatory compliance (HRRP).

**Approach**: We developed an end-to-end data pipeline using **Python** for cleaning 100k+ records, grouping 700+ clinical diagnoses, and performing statistical validation. The results were then visualized in a 3-part **Tableau** dashboard suite designed for both executive and clinical decision-makers.

**Key Insights**:
1.  **Prior Visits as the "Red Flag"**: Patients with 3+ prior inpatient visits are nearly **5x more likely** to be readmitted.
2.  **Age Risk Segmentation**: While geriatric patients (70-90) are high volume, the **25-35 age group** shows surprisingly high readmission intensity.
3.  **Treatment Impact**: Medication adjustments (dosage changes) are significantly correlated with improved stability and lower 30-day return rates.

**Key Recommendations**:
*   Implement mandatory **48-hour post-discharge follow-ups** for all "High Risk" patients (3+ prior visits).
*   Standardize **Medication Reconciliation** protocols specifically for patients transitioning between emergency and inpatient care.

---

## 3. Sector & Business Context
Hospital readmission is a multi-billion dollar challenge in the healthcare sector. In the US alone, the Hospital Readmissions Reduction Program (HRRP) penalizes hospitals with excessive readmission rates.
*   **Decision-Makers**: Hospital CEOs (Financial impact), Clinical Leads (Quality of care), and Discharge Planners (Operational flow).
*   **Business Value**: Reducing readmissions by even 2% can save a large hospital millions in penalties and free up critical bed capacity for elective surgeries.

---

## 4. Problem Statement & Objectives
**Formal Problem Definition**: To identify demographic, clinical, and medication-based patterns that predict 30-day hospital readmission in diabetic patients and provide actionable recommendations to reduce these occurrences.

**Objectives**:
1.  Standardize and clean a dataset of 100,000+ patient encounters.
2.  Perform statistical hypothesis testing to validate readmission drivers.
3.  Build a real-time Decision Support Dashboard in Tableau.

---

## 5. Data Description
*   **Source**: [UCI Machine Learning Repository - Diabetes Dataset](https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008)
*   **Structure**: 101,763 rows and 54 columns (after cleaning).
*   **Key Fields**: `Age`, `Race`, `Days in Hospital`, `Medication Changed`, `Prior Inpatient Visits`, and `Primary Diagnosis Group`.
*   **Limitations**: The data is retrospective (1999-2008), so current pharmaceutical trends (like GLP-1s) may not be fully represented.

---

## 6. Data Cleaning & ETL Pipeline
We built a robust 9-step pipeline in Python (`notebooks/02_cleaning.ipynb`):
1.  **Standardization**: Converted all `?` markers to clinical labels like "Unknown" or "Not Tested."
2.  **Noise Removal**: Dropped constant columns (`examide`, `citoglipton`) that provided zero analytical variance.
3.  **Clinical Mapping**: Mapped 30+ technical IDs (e.g., Admission Type = 1) to readable clinical strings ("Emergency").
4.  **Diagnosis Grouping**: Developed a custom mapping function to group 700+ ICD9 codes into **17 clinical categories** (e.g., Circulatory, Respiratory, Metabolic).
5.  **Feature Engineering**: Created binary target columns for `<30`, `>30`, and `NO` readmission.
6.  **Outlier Handling**: Capped hospital stay duration and medication counts at the 99th percentile.

---

## 7. KPI & Metric Framework
| KPI | Formula | Why it Matters |
| :--- | :--- | :--- |
| **30-Day Readmission Rate** | `SUM(<30) / COUNT(Encounters)` | Direct measure of discharge quality. |
| **Avg Length of Stay (LOS)** | `AVG(Days in Hospital)` | Measures operational efficiency. |
| **High-Risk Concentration** | `Count(Prior Visits >= 3)` | Identifies the top 5% of patients driving 40% of costs. |

---

## 8. Exploratory Data Analysis (EDA)
**Key Findings (from `notebooks/03_eda.ipynb`)**:
*   **Age Trend**: Readmission risk is not linear. It peaks at age 25 and then again at age 75.
*   **Race Comparison**: Caucasian and African American patients represent the highest volume, with Caucasian patients showing a slightly higher 30-day readmit rate.
*   **Medication Impact**: Patients with "Medication Change = Ch" during their stay show different recovery patterns compared to those with stable doses.

---

## 9. Statistical Analysis
We performed rigorous validation in `notebooks/04_statistical_analysis.ipynb`:
1.  **Mann-Whitney U Test**: Confirmed that Prior Inpatient Visits are a statistically significant predictor (p < 0.0001).
2.  **Independent T-Test**: Proved that readmitted patients stay **0.8 days longer** in the hospital than stable patients.
3.  **Random Forest Feature Importance**: Ranked **"Number of Inpatient Visits"** and **"Lab Procedures"** as the top two clinical markers for risk.

---

## 10. Tableau Dashboard Design
The dashboard suite consists of 3 dedicated views:
1.  **Executive Overview**: High-level KPIs and demographic risk segmentation.
2.  **Patient Risk Analysis**: A treemap of diagnoses and a bar chart showing the "Prior Visit" risk multiplier.
3.  **Treatment & Outcomes**: Impact of medication changes and insulin management.

*   **Interactive Elements**: Global filters for Age, Race, and Admission Source.
*   **Visual Proofs**:
    - **Dashboard 1**: Includes Readmission Rate (11.16%) and Age Risk analysis.
    - **Dashboard 2**: Visualizes the exponential risk increase as Prior Visits grow.
    - **Dashboard 3**: Focuses on Treatment Efficacy (Medication Change Impact).

---

## 11. Insights Summary
1.  **The Visit Multiplier**: A patient with 1 visit has a 15% risk; a patient with 4+ visits has a 60%+ risk.
2.  **Emergency Intensity**: 53.05% of all encounters originate in the Emergency Room, driving the majority of readmissions.
3.  **Diagnosis Focus**: **Circulatory** issues represent the highest volume of 30-day returns, followed by **Diabetes-specific** metabolic issues.
4.  **Stay Optimization**: Discharging patients before Day 3 may lead to "bounce-backs" if clinical stability is not fully achieved.

---

## 12. Recommendations
1.  **High-Risk Discharge Protocol**: Patients with **Prior Visits >= 3** must receive a "Social Determinants of Health" assessment before discharge.
2.  **Post-Discharge "Hotline"**: Establish a nurse-led callback program within **48 hours** for patients in the Circulatory diagnosis group.
3.  **Medication Reconciliation**: Formalize a secondary pharmacist review for any patient who had their **Insulin dosage adjusted** during their stay.

---

## 13. Impact Estimation
*   **Cost Savings**: Reducing readmissions by 5% could save an average 500-bed hospital ~$1.2M annually in penalties.
*   **Efficiency**: Lowering the average LOS by 0.2 days frees up ~2,000 bed-days per year.
*   **Stakeholder Urgency**: As healthcare shifts toward "Value-Based Care," readmission management is no longer optional—it is a financial necessity.

---

## 14. Limitations
*   **Data Age**: The dataset is from 1999-2008; patient demographics and treatments have evolved since then.
*   **Missing Data**: We lacked data on "Social Determinants" (Income, Housing), which are known to be strong readmission drivers.

---

## 15. Future Scope
1.  **Predictive Modeling**: Building a real-time Logistic Regression or XGBoost model inside the hospital EMR to flag "High Risk" at the moment of admission.
2.  **External Data Integration**: Linking census data to map readmission risk by neighborhood/zip code.

---

## 16. Conclusion
This project demonstrates that hospital readmissions are not random—they are predictable clinical patterns. By focusing on **Prior Visit volume** and **Treatment Stability**, hospitals can transition from "Reactive" to "Proactive" care, significantly reducing the 11.16% readmission rate and improving patient lives.

---

## 17. Appendix
*   **Data Dictionary**: Full 54-column documentation in `docs/data_dictionary.md`.
*   **ETL Pipeline Logic**: Full script in `scripts/etl_pipeline.py`.

---

## 18. Contribution Matrix
| Team Member | Dataset & Sourcing | ETL & Cleaning | EDA & Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT & Viva |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Dhanvin** | 100% | 100% | 80% | 100% | 10% | 20% | 80% |
| **Tanish Garg** | 0% | 0% | 10% | 0% | 45% | 10% | 10% |
| **Ayush** | 0% | 0% | 10% | 0% | 45% | 10% | 10% |
| **Sumit** | 0% | 0% | 0% | 0% | 0% | 30% | 0% |
| **Lakshay** | 0% | 0% | 0% | 0% | 0% | 30% | 0% |

**Declaration**: We confirm that the above contribution details are accurate and verifiable through GitHub Insights and committed files.

**Team Lead Signature**: *Dhanvin*
