import pandas as pd
import numpy as np
import os

def run_etl():
    raw_path = 'data/raw/diabetic_data.csv'
    processed_dir = 'data/processed'
    output_path = os.path.join(processed_dir, 'cleaned_diabetic_data.csv')

    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    df = pd.read_csv(raw_path)

    df.replace('?', np.nan, inplace=True)

    cols_to_drop = ['weight', 'payer_code', 'medical_specialty']
    df.drop(columns=cols_to_drop, inplace=True)

    age_map = {
        '[0-10)': 5, '[10-20)': 15, '[20-30)': 25, '[30-40)': 35, 
        '[40-50)': 45, '[50-60)': 55, '[60-70)': 65, '[70-80)': 75, 
        '[80-90)': 85, '[90-100)': 95
    }
    df['age'] = df['age'].map(age_map)

    df['readmit_30d'] = (df['readmitted'] == '<30').astype(int)
    df.drop(columns=['readmitted'], inplace=True)

    df = df[df['gender'] != 'Unknown/Invalid']
    df['race'].fillna('Other', inplace=True)

    df.to_csv(output_path, index=False)
    print(f"ETL Complete. Cleaned data saved to {output_path}")

if __name__ == "__main__":
    run_etl()
