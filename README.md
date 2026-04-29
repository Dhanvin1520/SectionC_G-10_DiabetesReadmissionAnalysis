# SectionC_G-10_DiabetesReadmissionAnalysis
Newton School of Technology | Data Visualization & Analytics | Capstone 2

## Project Overview
| Field | Details |
| :--- | :--- |
| **Project Title** | Diabetes Readmission Analysis: Predicting 30-Day Hospital Returns |
| **Sector** | Healthcare |
| **Team ID** | G-10 |
| **Section** | C |
| **Faculty Mentor** | Archit Raj |
| **Institute** | Newton School of Technology |
| **Submission Date** | April 29, 2026 |

## Team Members
| Role | Name | GitHub Username |
| :--- | :--- | :--- |
| **Project Lead** | Dhanvin Vadlamudi | Dhanvin1520 |
| **Tableau Architect** | Ayush Mittal | mittalayushh |
| **Data Engineer** | GARGI SRIVASTAVA | gigibyte2024 |
| **Statistical Analyst** | tanish Garg | tnshgarg |
| **EDA Specialist** | Sumit Yadav | sumit316-glitch |
| **Documentation & QA** | LAKSHYA | Lakshyalamba |

## Business Problem
Diabetic patients represent a significant portion of hospital admissions, and readmission rates remain a critical challenge for healthcare providers. This project analyzes a decade of clinical data from 130 US hospitals to identify factors contributing to patient readmissions within 30 days. By identifying high-risk characteristics and treatment patterns, hospital administrators can optimize discharge planning and post-care strategies to improve patient outcomes and reduce healthcare costs.

### Core Business Question
How can patient demographics, medication changes, and hospital treatment history be leveraged to accurately predict and reduce 30-day readmission rates in diabetic patients?

### Decision Supported
This analysis enables hospital management to identify high-risk patient segments prior to discharge and implement targeted intervention strategies, such as specialized follow-up care or medication adjustments, to prevent avoidable readmissions.

## Analytical Pipeline
The project follows a structured 7-step workflow:
1. **Define** - Sector selected (Healthcare), problem statement scoped, and mentor approval obtained.
2. **Extract** - Raw dataset sourced from UCI Repository and committed to `data/raw/`.
3. **Clean and Transform** - Cleaning pipeline built in `notebooks/02_cleaning.ipynb` handling missing values (`?`) and ICD-9 mapping.
4. **Analyze** - EDA and statistical analysis (Mann-Whitney U Test) performed in notebooks `03` and `04`.
5. **Visualize** - Interactive Tableau dashboard built and published on Tableau Public.
6. **Recommend** - Data-backed business recommendations delivered to support clinical decisions.
7. **Report** - Final project report and presentation deck completed.

## Dataset
| Attribute | Details |
| :--- | :--- |
| **Source Name** | UCI Machine Learning Repository (Diabetes 130-US Hospitals) |
| **Direct Access Link** | [Access Dataset](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) |
| **Row Count** | 101,763  |
| **Column Count** | 50 meaningful features |
| **Time Period Covered** | 1999 to 2008 |
| **Format** | CSV |

### Key Columns Used
| Column Name | Description | Role in Analysis |
| :--- | :--- | :--- |
| `readmitted` | Patient readmission status (NO, >30, <30) | **Target Variable** (KPI) |
| `number_inpatient` | Count of prior inpatient visits in the preceding year | **Primary Risk Predictor** |
| `time_in_hospital` | Total days spent in hospital during encounter | Operational Efficiency Metric |
| `age_midpoint` | Numerical representation of patient age intervals | Demographic Segmentation |

## KPI Framework
| KPI | Definition | Formula / Computation |
| :--- | :--- | :--- |
| **30-Day Readmission Rate (%)** | Percentage of patients readmitted within 30 days | `(Count '<30') / (Total Admissions) * 100` |
| **Avg Length of Stay (LOS)** | Average bed-occupancy duration per encounter | `Average(time_in_hospital)` |
| **Medication Stability Rate** | Percentage of patients with unchanged dosages | `(Count 'No Change') / (Total Encounters)` |

## Tableau Dashboard
*Decision support suite for hospital readmission risk management.*

### 🖥️ Dashboard Gallery
| Executive Overview | Patient Risk Analysis | Treatment & Outcomes |
| :---: | :---: | :---: |
| ![Executive View](tableau/screenshots/dashboard-1.png) | ![Risk Analysis](tableau/screenshots/dashboard-2.png) | ![Treatment Analysis](tableau/screenshots/dashboard-3.png)

- **Executive View**: High-level KPIs and readmission distribution by Age/Race.
- **Operational View**: Drill-down into diagnosis-specific risk and discharge patterns.
- **Outcome Analysis**: Correlation between medication titration and patient stability.
- **Dashboard URL**: [View Live on Tableau Public](https://public.tableau.com/app/profile/ayush.mittal4873/viz/DVACapstoneDiabetesReadmissionAnalysis_v2025_3/Dashboard_Executive_Overview?publish=yes)

## Key Insights
1. **Frequent Flyer Risk**: Patients with $\ge 3$ prior inpatient visits return at a 4.5x higher rate than the baseline.
2. **The Age Paradox**: While volume peaks at 70-80 years, a severe secondary risk peak exists in the 25-35 group (Type-1 management gap).
3. **Clinical Instability**: Patients undergoing medication "Down-titration" are 22% more likely to be readmitted early.
4. **Diagnosis Drivers**: Circulatory and Respiratory clusters account for 45% of all 30-day returns.
5. **Testing Gaps**: Patients without an A1C test during stay exhibit higher return rates than those with "Stable" results.
6. **Discharge Failures**: 15% of readmitted patients were discharged to "Home Care" without specialized follow-up despite high severity scores.
7. **Emergency Baseline**: Emergency admissions carry a 12% higher intrinsic risk than elective encounters.
8. **Stay Duration**: Readmission risk correlates positively with LOS, peaking for patients staying 7-10 days (severity proxy).

## Recommendations
| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | High Prior Visits | Implement 48-hour automated nurse callback for patients with $\ge 2$ prior stays. | 15% reduction in early returns. |
| 2 | Medication Instability | Physician sign-off required for discharge if insulin dosage was adjusted within 24 hours. | Improved clinical stability post-discharge. |
| 3 | Diagnosis Clusters | Standardized "Heart-Diabetes" discharge checklist for the Circulatory cluster. | Optimized specialized care routing. |
| 4 | Testing Gaps | Mandate A1C testing for all patients with LOS $> 3$ days. | Better long-term glycemic control. |

## Repository Structure
```text
SectionC_G-10_DiabetesReadmissionAnalysis/
|-- README.md
|-- requirements.txt              # Project dependencies
|-- data/
|   |-- raw/
|   |   `-- diabetic_data.csv        # Original UCI dataset
|   `-- processed/
|       |-- cleaned_diabetic_data.csv # Final pipeline output
|       `-- summary/                  # Aggregate risk summaries
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|-- scripts/
|   |-- __init__.py
|   `-- etl_pipeline.py              # Automated data cleaning script
|-- tableau/
|   |-- screenshots/                 # dashboard-1.png, dashboard-2.png, dashboard-3.png
|   `-- dashboard_links.md           # Interactive dashboard URL
|-- reports/
|   |-- Diabetes-Readmission-G10-Final.pdf   # Main Project Deliverable
|   `-- G_10_report.pdf                      # Technical Appendix
|-- docs/
|   `-- data_dictionary.md           # Dataset schema and definitions
|-- DVA-oriented-Resume/             # Team resumes and career assets
`-- DVA-focused-Portfolio/            # Project showcase links
```

## Tech Stack
| Tool | Purpose |
| :--- | :--- |
| **Python** | ETL, Cleaning, and Statistical Analysis |
| **Tableau Public** | Dashboard design and visualization |
| **GitHub** | Version control and collaboration |

## Contribution Matrix
| Team Member | Dataset | ETL | EDA | Stats | Tableau | Report | PPT |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Dhanvin Vadlamudi** | ✅ | ✅ | ✅ | ✅ | | ✅ | ✅ |
| **Ayush Mittal** | ✅ | ✅ | | | ✅ | | |
| **GARGI SRIVASTAVA** | ✅ | | | | ✅ | | |
| **tanish Garg** | ✅ | | | | ✅ | | |
| **Sumit Yadav** | ✅ | | | | | ✅ | |
| **LAKSHYA** | ✅ | | | | | | ✅ |

**Declaration:** We confirm that the above contribution details are accurate and verifiable through GitHub Insights and PR history.

**Team Lead Name:** Dhanvin Vadlamudi  
**Date:** April 29, 2026

---
*Newton School of Technology - Data Visualization & Analytics | Capstone 2*
