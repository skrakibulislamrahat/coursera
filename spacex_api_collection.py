import pandas as pd

def load_api_style_data(csv_path="dataset_part_2.csv"):
    """
    For the capstone support package, this reads the prepared CSV that mirrors
    the flattened SpaceX launch table normally produced from pd.json_normalize.
    """
    df = pd.read_csv(csv_path)
    print("Rows, columns:", df.shape)
    print(df.head())
    return df

if __name__ == "__main__":
    df = load_api_style_data()
    print("First static-fire-like year example:", pd.to_datetime(df["Date"]).dt.year.iloc[0])
