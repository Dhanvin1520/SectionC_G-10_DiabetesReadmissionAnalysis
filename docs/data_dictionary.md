# Data Dictionary - Diabetes Readmission Analysis

This document is the official metadata record for the project. It has been updated to reflect the features available after **Notebook 02: Cleaning**.

## Status: ETL & Cleaning Complete (Apr 20, 2026)

### 1. Patient Demographics & Identification
| Column | Description | Type | Transformation |
| :--- | :--- | :--- | :--- |
| `encounter_id` | Unique identifier of an encounter | ID | None |
| `patient_nbr` | Unique identifier of a patient | ID | None |
| `race` | Patient's race | Categorical | Missing values imputed as 'Other' |
| `gender` | Patient's gender | Categorical | 'Unknown/Invalid' records dropped |
| `age` | Patient's age interval | **Numerical** | Recoded to bin midpoints (e.g., [40-50) -> 45) |

### 2. Clinical Encounter Metrics
| Column | Description | Type | Transformation |
| :--- | :--- | :--- | :--- |
| `admission_type_id` | Integer identifier for admission type | Discrete | None |
| `discharge_disposition_id` | Integer identifier for discharge goal | Discrete | None |
| `admission_source_id` | Integer identifier for admission source | Discrete | None |
| `time_in_hospital` | Number of days in hospital | Numerical | None |
| `num_lab_procedures` | No. of lab tests in encounter | Numerical | None |
| `num_procedures` | No. of non-lab procedures | Numerical | None |
| `num_medications` | No. of generic meds prescribed | Numerical | None |
| `number_outpatient` | Outpatient visits in preceding year | Numerical | None |
| `number_emergency` | Emergency visits in preceding year | Numerical | None |
| `number_inpatient` | Inpatient visits in preceding year | Numerical | None |
| `diag_1`, `diag_2`, `diag_3` | Primary, secondary, and tertiary diagnoses | ICD9 Codes | None |
| `number_diagnoses` | Number of diagnosis entries | Numerical | None |

### 3. Medication & Management
| Column | Description | Type | Transformation |
| :--- | :--- | :--- | :--- |
| `max_glu_serum` | Results of glucose serum test | Categorical | None |
| `A1Cresult` | Results of A1C test | Categorical | None |
| `change` | Indicates if there was a change in diabetic meds | Binary | None |
| `diabetesMed` | Indicates if any diabetic medication was prescribed | Binary | None |

### 4. Target Variables
| Column | Description | Type | Transformation |
| :--- | :--- | :--- | :--- |
| **`readmit_30d`** | **Primary KPI Target** | **Binary** | Created from original `readmitted` (1 if <30 days, else 0) |

## Dropped Columns (Low Quality/High Missingness)
- `weight`: $>90\%$ missing.
- `payer_code`: $>40\%$ missing / irrelevant for clinical prediction.
- `medical_specialty`: $>40\%$ missing.
