from extract import extract_data
from transform import transform_data
from load import load_data

if __name__ == "__main__":

    INPUT_FILE = "training.1600000.processed.noemoticon.csv"
    OUTPUT_FILE = "processed_data.csv"

    # Extract
    df_raw = extract_data(INPUT_FILE)

    # Transform
    df_transformed = transform_data(df_raw)

    # Load
    load_data(df_transformed, OUTPUT_FILE)