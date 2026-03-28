import pandas as pd
from sklearn.model_selection import train_test_split

def wrangle_data(csv_path="dataset_part_2.csv"):
    df = pd.read_csv(csv_path)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year
    df["LandingPad"] = df["LandingPad"].fillna("Unknown")
    features = df[[
        "FlightNumber","PayloadMass","Orbit","LaunchSite","Flights","GridFins",
        "Reused","Legs","LandingPad","Block","ReusedCount","Serial","Year",
        "Latitude","Longitude"
    ]].copy()
    X = pd.get_dummies(features, columns=["Orbit","LaunchSite","LandingPad","Serial"], drop_first=False)
    y = df["Class"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=2, stratify=y
    )
    print("Feature matrix shape:", X.shape)
    print("Train shape:", X_train.shape, "Test shape:", X_test.shape)
    return df, X, y, X_train, X_test, y_train, y_test

if __name__ == "__main__":
    wrangle_data()
