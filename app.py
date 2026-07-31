
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

# Feature names
FEATURES = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]


# Home page
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Heart Disease Prediction API is running!",
        "endpoint": "/predict",
        "method": "POST"
    })


# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        # Check for missing features
        missing_features = [
            feature for feature in FEATURES
            if feature not in data
        ]

        if missing_features:
            return jsonify({
                "error": "Missing features",
                "missing": missing_features
            }), 400

        # Convert input to DataFrame
        input_data = pd.DataFrame(
            [[data[feature] for feature in FEATURES]],
            columns=FEATURES
        )

        # Make prediction
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            result = "Heart Disease Detected"
        else:
            result = "No Heart Disease"

        return jsonify({
            "prediction": result
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 400


# Run application
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
