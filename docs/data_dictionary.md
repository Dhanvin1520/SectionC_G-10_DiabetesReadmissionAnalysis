# Data Dictionary - Diabetes Readmission Analysis

This document describes the complete feature set available in `data/processed/cleaned_diabetic_data.csv` after the ETL pipeline was applied to the raw dataset.

## Cleaning Summary

| Step | Action | Rationale |
| :--- | :--- | :--- |
| 1 | Replaced all `?` with `NaN`, then imputed | Raw data used `?` as a missing indicator |
| 2 | Removed 3 records with `Unknown/Invalid` gender | Invalid demographic data |
| 3 | Dropped 2 constant columns (`examide`, `citoglipton`) | Both contained only one value (`No`) across all 101k records — zero analytical value |
| 4 | Imputed `race` as `Unknown`, `weight` as `Not Recorded`, `payer_code`/`medical_specialty` as `Unknown` | Preserves rows while marking missingness explicitly |
| 5 | Imputed `max_glu_serum` and `A1Cresult` as `Not Tested` | Clinical tests not performed on all patients |
| 6 | Mapped `age` intervals to numerical midpoints | Enables correlation and statistical analysis |
| 7 | Mapped `admission_type_id`, `discharge_disposition_id`, `admission_source_id` to clinical labels | Raw IDs are not interpretable in dashboards |
| 8 | Classified ICD9 diagnosis codes into 17 clinical groups | Enables high-level diagnosis pattern analysis |
| 9 | Created 3 readmission target columns | Allows tracking of under-30, over-30, and never-readmitted cohorts |
| 10 | Renamed all columns to Tableau-friendly labels | Professional dashboard readability |

## Final Dataset: 101,763 rows × 54 columns | Zero Null Values

---

## Patient Identification
| Column | Description | Type |
| :--- | :--- | :--- |
| `Encounter ID` | Unique identifier for each hospital encounter | ID |
| `Patient ID` | Unique identifier for each patient (can have multiple encounters) | ID |

## Demographics
| Column | Description | Type | Values |
| :--- | :--- | :--- | :--- |
| `Race` | Patient's race | Categorical | Caucasian, AfricanAmerican, Hispanic, Asian, Other, Unknown |
| `Gender` | Patient's gender | Categorical | Female, Male |
| `Age` | Age interval converted to midpoint | Numerical | 5, 15, 25, 35, 45, 55, 65, 75, 85, 95 |
| `Weight` | Weight range of patient | Categorical | Multiple ranges or `Not Recorded` |

## Admission Details
| Column | Description | Type | Sample Values |
| :--- | :--- | :--- | :--- |
| `Admission Type` | How the patient was admitted | Categorical | Emergency, Urgent, Elective, Newborn, Trauma Center |
| `Discharge Disposition` | Where the patient went after discharge | Categorical | Discharged to Home, SNF Transfer, Expired, Hospice, etc. |
| `Admission Source` | Where the patient came from | Categorical | Emergency Room, Physician Referral, Transfer from Hospital, etc. |
| `Payer Code` | Insurance payer code | Categorical | 18 categories including Unknown |
| `Medical Specialty` | Specialty of the admitting physician | Categorical | 73 specialties including Unknown |

## Clinical Encounter Metrics
| Column | Description | Type |
| :--- | :--- | :--- |
| `Days in Hospital` | Number of days between admission and discharge | Numerical (1–14) |
| `Lab Procedures` | Number of lab tests performed during encounter | Numerical |
| `Non-Lab Procedures` | Number of non-lab procedures performed | Numerical |
| `Number of Medications` | Number of distinct generic medications prescribed | Numerical |
| `Total Diagnoses` | Number of diagnoses entered to the system | Numerical |

## Prior Visit History
| Column | Description | Type |
| :--- | :--- | :--- |
| `Prior Outpatient Visits` | Number of outpatient visits in the preceding year | Numerical |
| `Prior Emergency Visits` | Number of emergency visits in the preceding year | Numerical |
| `Prior Inpatient Visits` | Number of inpatient visits in the preceding year | Numerical |

## Diagnosis Information
| Column | Description | Type |
| :--- | :--- | :--- |
| `Primary Diagnosis (ICD9)` | Raw ICD9 code for the primary diagnosis | Code |
| `Secondary Diagnosis (ICD9)` | Raw ICD9 code for the secondary diagnosis | Code |
| `Additional Diagnosis (ICD9)` | Raw ICD9 code for the additional diagnosis | Code |
| `Primary Diagnosis Group` | Classified clinical group (e.g., Circulatory, Diabetes) | Categorical (17 groups) |
| `Secondary Diagnosis Group` | Classified clinical group for secondary diagnosis | Categorical (17 groups) |
| `Additional Diagnosis Group` | Classified clinical group for additional diagnosis | Categorical (17 groups) |

## Lab Test Results
| Column | Description | Type | Values |
| :--- | :--- | :--- | :--- |
| `Glucose Serum Test` | Results of glucose serum test | Categorical | Norm, >200, >300, Not Tested |
| `A1C Result` | Results of A1C test | Categorical | Norm, >7, >8, Not Tested |

## Medication Status (Per Drug)
Each medication column indicates whether the drug was changed during the encounter.

| Values | Meaning |
| :--- | :--- |
| `No` | Not prescribed |
| `Steady` | Prescribed, dosage unchanged |
| `Up` | Dosage was increased |
| `Down` | Dosage was decreased |

**Medications tracked**: Metformin, Repaglinide, Nateglinide, Chlorpropamide, Glimepiride, Acetohexamide, Glipizide, Glyburide, Tolbutamide, Pioglitazone, Rosiglitazone, Acarbose, Miglitol, Troglitazone, Tolazamide, Insulin, Glyburide-Metformin, Glipizide-Metformin, Glimepiride-Pioglitazone, Metformin-Rosiglitazone, Metformin-Pioglitazone

## Treatment Decisions
| Column | Description | Type | Values |
| :--- | :--- | :--- | :--- |
| `Medication Changed` | Whether any diabetic medication was changed | Binary | Ch (Changed), No |
| `Diabetes Medication Prescribed` | Whether any diabetic medication was prescribed | Binary | Yes, No |

## Target Variables
| Column | Description | Type | Values |
| :--- | :--- | :--- | :--- |
| `Readmission Status` | Original readmission outcome | Categorical | NO, >30, <30 |
| **`Readmitted Under 30 Days`** | **Primary KPI**: Was patient readmitted within 30 days? | Binary | 1 = Yes, 0 = No |
| **`Readmitted After 30 Days`** | Was patient readmitted after 30 days? | Binary | 1 = Yes, 0 = No |
| **`Not Readmitted`** | Was patient never readmitted? | Binary | 1 = Yes, 0 = No |
