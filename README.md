# SectionC_G-10_DiabetesReadmissionAnalysis
Newton School of Technology | Data Visualization & Analytics | Capstone 2

## Project Overview
| Field | Details |
| :--- | :--- |
| **Project Title** | Diabetes Readmission Analysis: Predicting 30-Day Hospital Returns |
| **Sector** | Healthcare |
| **Team ID** | G-10 |
| **Section** | C |
| **Faculty Mentor** | To be assigned |
| **Institute** | Newton School of Technology |
| **Submission Date** | April 28, 2026 |

## Team Members
| Role | Name | GitHub Username |
| :--- | :--- | :--- |
| **Project Lead** | Dhanvin Vadlamudi | Dhanvin1520 |
| **Data Lead** | Ayush Mittal | mittalayushh |
| **ETL Lead** | GARGI SRIVASTAVA | gigibyte2024 |
| **Analysis Lead** | LAKSHYA | Lakshyalamba |
| **Visualization Lead** | Sumit Yadav | sumit316-glitch |
| **Strategy Lead** | tanish Garg | tnshgarg |

## Business Problem
Diabetic patients represent a significant portion of hospital admissions, and readmission rates remain a critical challenge for healthcare providers. This project analyzes a decade of clinical data from 130 US hospitals to identify factors contributing to patient readmissions within 30 days. By identifying high-risk characteristics and treatment patterns, hospital administrators can optimize discharge planning and post-care strategies to improve patient outcomes and reduce healthcare costs.

### Core Business Question
How can patient demographics, medication changes, and hospital treatment history be leveraged to accurately predict and reduce 30-day readmission rates in diabetic patients?

### Decision Supported
This analysis enables hospital management to identify high-risk patient segments prior to discharge and implement targeted intervention strategies, such as specialized follow-up care or medication adjustments, to prevent avoidable readmissions.

## Dataset
| Attribute | Details |
| :--- | :--- |
| **Source Name** | UCI Machine Learning Repository |
| **Direct Access Link** | [Diabetes 130-US Hospitals Dataset](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) |
| **Row Count** | 101,766 |
| **Column Count** | 50 |
| **Time Period Covered** | 1999 to 2008 |
| **Format** | CSV |

### Key Columns Used
| Column Name | Description | Role in Analysis |
| :--- | :--- | :--- |
| `readmitted` | Patient readmission status (NO, >30, <30) | **Target Variable** (KPI 1) |
| `time_in_hospital` | Number of days between admission and discharge | **Target Variable** (KPI 2) |
| `age` | Age interval of the patient | Segmentation / Filter |
| `number_inpatient` | Number of inpatient visits of the patient in the year preceding the encounter | Predictor / Segment |

## KPI Framework
| KPI | Definition | Formula / Computation |
| :--- | :--- | :--- |
| **30-Day Readmission Rate (%)** | Percentage of patients readmitted within 30 days of discharge | `(Count of patients with readmitted = '<30') / (Total Admissions) * 100` |
| **Average Length of Stay (Days)** | Average time patients spend in the hospital | `Average(time_in_hospital)` |

## Tableau Dashboard
*Detailed Tableau link and screenshots will be added in Phase 2.*
- **Dashboard URL**: [To be added]
- **Executive View**: Summary of readmission rates across age groups and medical specialties.
- **Operational View**: Detailed breakdown of length of stay vs. medication changes.

## Repository Structure
```
SectionC_G-10_DiabetesReadmissionAnalysis/
|-- README.md
|-- data/
|   |-- raw/                         # Original dataset (diabetic_data.csv)
|   `-- processed/                   # Cleaned output from ETL pipeline
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|-- scripts/
|   `-- etl_pipeline.py
|-- tableau/
|   |-- screenshots/
|   `-- dashboard_links.md
|-- reports/
|   |-- project_report_template.md
|   `-- presentation_outline.md
|-- docs/
|   `-- data_dictionary.md
|-- DVA-oriented-Resume/
`-- DVA-focused-Portfolio/
```

## Tech Stack
| Tool | Purpose |
| :--- | :--- |
| **Python** | ETL, Cleaning, and Statistical Analysis |
| **Tableau Public** | Dashboard design and visualization |
| **GitHub** | Version control and collaboration |

## Academic Integrity
We confirm that the analysis, code, and recommendations in this repository are the original work of the team listed above.
