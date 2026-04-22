import pandas as pd
import numpy as np
import os

def classify_icd9(code):
    if pd.isnull(code):
        return 'Unknown'
    code = str(code).strip()
    if code.startswith('V') or code.startswith('E'):
        return 'External/Supplementary'
    try:
        val = float(code)
    except ValueError:
        return 'Unknown'

    if 250 <= val < 251:
        return 'Diabetes'
    elif 390 <= val <= 459 or val == 785:
        return 'Circulatory'
    elif 460 <= val <= 519 or val == 786:
        return 'Respiratory'
    elif 520 <= val <= 579 or val == 787:
        return 'Digestive'
    elif 580 <= val <= 629 or val == 788:
        return 'Genitourinary'
    elif 710 <= val <= 739:
        return 'Musculoskeletal'
    elif 800 <= val <= 999:
        return 'Injury/Poisoning'
    elif 140 <= val <= 239:
        return 'Neoplasms'
    elif 240 <= val <= 279:
        return 'Endocrine/Metabolic'
    elif 280 <= val <= 289:
        return 'Blood Disorders'
    elif 290 <= val <= 319:
        return 'Mental Disorders'
    elif 320 <= val <= 389:
        return 'Nervous System'
    elif 680 <= val <= 709:
        return 'Skin/Subcutaneous'
    elif 1 <= val <= 139:
        return 'Infectious/Parasitic'
    else:
        return 'Other'


def run_perfect_pipeline():
    raw_path = 'data/raw/diabetic_data.csv'
    processed_dir = 'data/processed'
    output_path = os.path.join(processed_dir, 'cleaned_diabetic_data.csv')

    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    df = pd.read_csv(raw_path)
    print(f"Raw dataset: {df.shape[0]} rows x {df.shape[1]} columns")

    df.replace('?', np.nan, inplace=True)

    df = df[df['gender'] != 'Unknown/Invalid']

    constant_cols = [col for col in df.columns if df[col].nunique() <= 1]
    df.drop(columns=constant_cols, inplace=True)
    print(f"Dropped {len(constant_cols)} constant columns: {constant_cols}")

    df['race'] = df['race'].fillna('Unknown')
    df['weight'] = df['weight'].fillna('Not Recorded')
    df['payer_code'] = df['payer_code'].fillna('Unknown')
    df['medical_specialty'] = df['medical_specialty'].fillna('Unknown')
    df['diag_1'] = df['diag_1'].fillna('Unknown')
    df['diag_2'] = df['diag_2'].fillna('Unknown')
    df['diag_3'] = df['diag_3'].fillna('Unknown')
    df['max_glu_serum'] = df['max_glu_serum'].fillna('Not Tested')
    df['A1Cresult'] = df['A1Cresult'].fillna('Not Tested')

    age_map = {
        '[0-10)': 5, '[10-20)': 15, '[20-30)': 25, '[30-40)': 35,
        '[40-50)': 45, '[50-60)': 55, '[60-70)': 65, '[70-80)': 75,
        '[80-90)': 85, '[90-100)': 95
    }
    df['age'] = df['age'].map(age_map)

    admission_type_map = {
        1: 'Emergency', 2: 'Urgent', 3: 'Elective', 4: 'Newborn',
        5: 'Not Available', 6: 'Not Available', 7: 'Trauma Center', 8: 'Not Available'
    }
    df['admission_type_id'] = df['admission_type_id'].map(admission_type_map).fillna('Other')

    discharge_map = {
        1: 'Discharged to Home', 2: 'Short-term Hospital Transfer',
        3: 'SNF Transfer', 4: 'ICF Transfer', 5: 'Another Facility Transfer',
        6: 'Home Health Service', 7: 'AMA (Left Against Advice)',
        8: 'Home Health Service', 9: 'Admitted as Inpatient',
        10: 'Neonate Transfer', 11: 'Expired', 12: 'Still Patient',
        13: 'Hospice/Home', 14: 'Hospice/Medical Facility',
        15: 'Swing Bed', 16: 'Another Rehab Facility',
        17: 'Another Rehab Facility', 18: 'Not Available',
        19: 'Expired (Admit)', 20: 'Expired (Home)', 21: 'Expired (Medical)',
        22: 'Rehab/Long-term', 23: 'Long-term Care Hospital',
        24: 'Nursing Facility (Medicaid)', 25: 'Not Available',
        27: 'Federal Healthcare', 28: 'Psychiatric Hospital'
    }
    df['discharge_disposition_id'] = df['discharge_disposition_id'].map(discharge_map).fillna('Other')

    admission_source_map = {
        1: 'Physician Referral', 2: 'Clinic Referral', 3: 'HMO Referral',
        4: 'Transfer from Hospital', 5: 'Transfer from SNF',
        6: 'Transfer from Another Facility', 7: 'Emergency Room',
        8: 'Court/Law Enforcement', 9: 'Not Available',
        10: 'Transfer from Critical Access', 11: 'Normal Delivery',
        13: 'Normal Delivery', 14: 'Normal Delivery',
        17: 'Not Available', 20: 'Not Available',
        22: 'Transfer from Hospital (Extramural)', 25: 'Transfer from Ambulatory Surgery'
    }
    df['admission_source_id'] = df['admission_source_id'].map(admission_source_map).fillna('Other')

    df['diag_1_group'] = df['diag_1'].apply(classify_icd9)
    df['diag_2_group'] = df['diag_2'].apply(classify_icd9)
    df['diag_3_group'] = df['diag_3'].apply(classify_icd9)

    df['readmit_under_30'] = (df['readmitted'] == '<30').astype(int)
    df['readmit_over_30'] = (df['readmitted'] == '>30').astype(int)
    df['not_readmitted'] = (df['readmitted'] == 'NO').astype(int)

    rename_map = {
        'encounter_id': 'Encounter ID',
        'patient_nbr': 'Patient ID',
        'race': 'Race',
        'gender': 'Gender',
        'age': 'Age',
        'weight': 'Weight',
        'admission_type_id': 'Admission Type',
        'discharge_disposition_id': 'Discharge Disposition',
        'admission_source_id': 'Admission Source',
        'time_in_hospital': 'Days in Hospital',
        'payer_code': 'Payer Code',
        'medical_specialty': 'Medical Specialty',
        'num_lab_procedures': 'Lab Procedures',
        'num_procedures': 'Non-Lab Procedures',
        'num_medications': 'Number of Medications',
        'number_outpatient': 'Prior Outpatient Visits',
        'number_emergency': 'Prior Emergency Visits',
        'number_inpatient': 'Prior Inpatient Visits',
        'diag_1': 'Primary Diagnosis (ICD9)',
        'diag_2': 'Secondary Diagnosis (ICD9)',
        'diag_3': 'Additional Diagnosis (ICD9)',
        'diag_1_group': 'Primary Diagnosis Group',
        'diag_2_group': 'Secondary Diagnosis Group',
        'diag_3_group': 'Additional Diagnosis Group',
        'number_diagnoses': 'Total Diagnoses',
        'max_glu_serum': 'Glucose Serum Test',
        'A1Cresult': 'A1C Result',
        'change': 'Medication Changed',
        'diabetesMed': 'Diabetes Medication Prescribed',
        'readmitted': 'Readmission Status',
        'readmit_under_30': 'Readmitted Under 30 Days',
        'readmit_over_30': 'Readmitted After 30 Days',
        'not_readmitted': 'Not Readmitted',
        'metformin': 'Metformin',
        'repaglinide': 'Repaglinide',
        'nateglinide': 'Nateglinide',
        'chlorpropamide': 'Chlorpropamide',
        'glimepiride': 'Glimepiride',
        'acetohexamide': 'Acetohexamide',
        'glipizide': 'Glipizide',
        'glyburide': 'Glyburide',
        'tolbutamide': 'Tolbutamide',
        'pioglitazone': 'Pioglitazone',
        'rosiglitazone': 'Rosiglitazone',
        'acarbose': 'Acarbose',
        'miglitol': 'Miglitol',
        'troglitazone': 'Troglitazone',
        'tolazamide': 'Tolazamide',
        'insulin': 'Insulin',
        'glyburide-metformin': 'Glyburide-Metformin',
        'glipizide-metformin': 'Glipizide-Metformin',
        'glimepiride-pioglitazone': 'Glimepiride-Pioglitazone',
        'metformin-rosiglitazone': 'Metformin-Rosiglitazone',
        'metformin-pioglitazone': 'Metformin-Pioglitazone'
    }
    df.rename(columns=rename_map, inplace=True)

    assert df.isnull().sum().sum() == 0, "There are still null values!"

    df.to_csv(output_path, index=False)

    print(f"\n✅ Perfect Dataset Generated: {output_path}")
    print(f"📋 Final Shape: {df.shape[0]} rows x {df.shape[1]} columns")

if __name__ == "__main__":
    run_perfect_pipeline()
