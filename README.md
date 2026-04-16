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
| **Analysis Lead** | tanish Garg | tnshgarg |
| **Visualization Lead** | Sumit Yadav | sumit316-glitch |
| **Strategy Lead** | Dhanvin Vadlamudi | Dhanvin1520 |
| **PPT and Quality Lead** | LAKSHYA | Lakshyalamba |

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

## Evaluation Rubric
| Area | Marks | Focus |
| :--- | :--- | :--- |
| **Problem Framing** | 10 | Is the business question clear and well-scoped? |
| **Data Quality and ETL** | 15 | Is the cleaning pipeline thorough and documented? |
| **Analysis Depth** | 25 | Are statistical methods applied correctly with insight? |
| **Dashboard and Visualization** | 20 | Is the Tableau dashboard interactive and decision-relevant? |
| **Business Recommendations** | 20 | Are insights actionable and well-reasoned? |
| **Storytelling and Clarity** | 10 | Is the presentation professional and coherent? |
| **Total** | **100** | |

## Submission Checklist
### GitHub Repository
- [x] Public repository created with the correct naming convention (`SectionName_TeamID_ProjectName`)
- [x] All notebooks committed in `.ipynb` format
- [x] `data/raw/` contains the original, unedited dataset
- [ ] `data/processed/` contains the cleaned pipeline output
- [ ] `tableau/screenshots/` contains dashboard screenshots
- [ ] `tableau/dashboard_links.md` contains the Tableau Public URL
- [ ] `docs/data_dictionary.md` is complete
- [x] `README.md` explains the project, dataset, and team
- [x] All members have visible commits and pull requests

### Tableau Dashboard
- [ ] Published on Tableau Public and accessible via public URL
- [ ] At least one interactive filter included
- [ ] Dashboard directly addresses the business problem

### Project Report
- [ ] Final report exported as PDF into `reports/`
- [ ] Cover page, executive summary, sector context, problem statement
- [ ] Data description, cleaning methodology, KPI framework
- [ ] EDA with written insights, statistical analysis results
- [ ] Dashboard screenshots and explanation
- [ ] 8-12 key insights in decision language
- [ ] 3-5 actionable recommendations with impact estimates

### Presentation Deck
- [ ] Final presentation exported as PDF into `reports/`
- [ ] Title slide through recommendations, impact, limitations, and next steps

### Individual Assets
- [ ] DVA-oriented resume updated to include this capstone
- [ ] Portfolio link or project case study added

## Contribution Matrix
| Team Member | Dataset & Sourcing | ETL & Cleaning | EDA & Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT & Viva |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Dhanvin Vadlamudi** | Support | Support | Support | Support | Support | Owner | Owner |
| **Ayush Mittal** | Owner | Support | Support | Support | Support | Support | Support |
| **GARGI SRIVASTAVA** | Support | Owner | Support | Support | Support | Support | Support |
| **tanish Garg** | Support | Support | Owner | Owner | Support | Support | Support |
| **Sumit Yadav** | Support | Support | Support | Support | Owner | Support | Support |
| **LAKSHYA** | Support | Support | Support | Support | Support | Support | Owner |

**Declaration:** We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts.

**Team Lead Name:** Dhanvin Vadlamudi  
**Date:** April 16, 2026

## Academic Integrity
All analysis, code, and recommendations in this repository are the original work of the team listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.
