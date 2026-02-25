import pandas as pd

def load_data(df: pd.DataFrame, output_path: str):
    
    print("Loading data...")

    df.to_csv(output_path, index=False)

    print("ETL Completed Successfully.")