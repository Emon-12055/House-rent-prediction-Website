import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# -----------------------------------
# 1. Find project folders
# -----------------------------------

BASE_DIR = Path(__file__).resolve().parents[3]

DATASET_PATH = BASE_DIR / "dataset" / "house_rent.csv"

MODEL_PATH = BASE_DIR / "predictor" / "ML" / "rent_model.pkl"


# -----------------------------------
# 2. Load dataset
# -----------------------------------

data = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully!")
print("Number of rows:", len(data))
print("Columns:", list(data.columns))


# -----------------------------------
# 3. Input features and target
# -----------------------------------

X = data[
    [
        "location",
        "bedrooms",
        "bathrooms",
        "size",
        "floor",
        "parking",
        "furnished",
        "balcony"
    ]
]

y = data["rent"]


# -----------------------------------
# 4. Separate categorical features
# -----------------------------------

categorical_features = [
    "location",
    "parking",
    "furnished",
    "balcony"
]

numerical_features = [
    "bedrooms",
    "bathrooms",
    "size",
    "floor"
]


# -----------------------------------
# 5. Convert text into numbers
# -----------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# -----------------------------------
# 6. Create Random Forest model
# -----------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# -----------------------------------
# 7. Create complete pipeline
# -----------------------------------

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# -----------------------------------
# 8. Split dataset
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# -----------------------------------
# 9. Train model
# -----------------------------------

print("Training model...")

pipeline.fit(X_train, y_train)

print("Model training completed!")


# -----------------------------------
# 10. Test model
# -----------------------------------

y_pred = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("--------------------------------")
print("Model Evaluation")
print("--------------------------------")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)


# -----------------------------------
# 11. Save trained model
# -----------------------------------

joblib.dump(pipeline, MODEL_PATH)

print("--------------------------------")
print("Model saved successfully!")
print("Saved at:", MODEL_PATH)