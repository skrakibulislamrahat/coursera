import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def build_data(csv_path="dataset_part_2.csv"):
    df = pd.read_csv(csv_path)
    df["Year"] = pd.to_datetime(df["Date"]).dt.year
    X = df[[
        "FlightNumber","PayloadMass","Orbit","LaunchSite","Flights","GridFins",
        "Reused","Legs","LandingPad","Block","ReusedCount","Year","Latitude","Longitude"
    ]]
    y = df["Class"]
    num_cols = ["FlightNumber","PayloadMass","Flights","GridFins","Reused","Legs","Block","ReusedCount","Year","Latitude","Longitude"]
    cat_cols = ["Orbit","LaunchSite","LandingPad"]

    preprocessor = ColumnTransformer([
        ("num", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]), num_cols),
        ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), cat_cols),
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=2, stratify=y
    )
    return preprocessor, X_train, X_test, y_train, y_test

def run_models():
    preprocessor, X_train, X_test, y_train, y_test = build_data()

    models = {
        "Logistic Regression": LogisticRegression(max_iter=2000),
        "SVM (RBF)": SVC(kernel="rbf", C=1.0, gamma="scale"),
        "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=2),
        "KNN": KNeighborsClassifier(n_neighbors=5)
    }

    for name, model in models.items():
        pipe = Pipeline([("prep", preprocessor), ("model", model)])
        pipe.fit(X_train, y_train)
        pred = pipe.predict(X_test)
        print("\n", name)
        print("Accuracy:", round(accuracy_score(y_test, pred), 4))
        print(confusion_matrix(y_test, pred))

if __name__ == "__main__":
    run_models()
