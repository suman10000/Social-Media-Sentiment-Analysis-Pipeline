import pandas as pd

COLUMN_NAMES = ["target", "id", "date", "flag", "user", "text"]

def extract_data(file_path: str) -> pd.DataFrame:

    print("Extracting data...")

    df = pd.read_csv(
        file_path,
        encoding="latin-1",
        names=COLUMN_NAMES
    )

    print("Data Loaded Successfully")
    print(df.head())

    return df