# Data Dictionary - Diabetes Readmission Analysis

This document describes the features used in the Analysis of Diabetes 130-US Hospitals Dataset.

## Patient Demographics
| Column | Description | Type |
| :--- | :--- | :--- |
| `race` | Patient's race (Caucasian, Asian, African American, etc.) | Categorical |
| `gender` | Patient's gender (Male, Female) | Categorical |
| `age` | Age interval transformed to a numerical midpoint | Numerical |

## Hospital Encounter Details
| Column | Description | Type |
| :--- | :--- | :--- |
| `time_in_hospital` | Number of days between admission and discharge | Numerical (Days) |
| `num_lab_procedures` | Number of lab tests performed during encounter | Numerical |
| `num_procedures` | Number of non-lab procedures performed | Numerical |
| `num_medications` | Number of distinct generic medications prescribed | Numerical |
| `number_outpatient` | Number of outpatient visits in the preceding year | Numerical |
| `number_emergency` | Number of emergency visits in the preceding year | Numerical |
| `number_inpatient` | Number of inpatient visits in the preceding year | Numerical |
| `number_diagnoses` | Number of diagnoses entered to the system | Numerical |

## Medication & Treatment
| Column | Description | Type |
| :--- | :--- | :--- |
| `change` | Indicates if there was a change in diabetic medications | Binary (Ch/No) |
| `diabetesMed` | Indicates if any diabetic medication was prescribed | Binary (Yes/No) |

## Target Variable
| Column | Description | Type |
| :--- | :--- | :--- |
| **`readmission_30d`** | Whether the patient was readmitted within 30 days | Binary (1/0) |
