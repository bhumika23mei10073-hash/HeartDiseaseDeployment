
# Heart Disease Prediction using Machine Learning

## Project Overview

This project predicts whether a patient is at risk of heart disease using machine learning.

A Logistic Regression model is trained using the Heart Disease Dataset. The trained model is saved using Joblib and served using a Flask REST API. The project is uploaded to GitHub and deployed on Render.

## Dataset

Dataset: Heart Disease Dataset

Source: Kaggle

Target Variable: target

- 0 = No Heart Disease
- 1 = Heart Disease

## Features Used

- age
- sex
- cp
- trestbps
- chol
- fbs
- restecg
- thalach
- exang
- oldpeak
- slope
- ca
- thal

## Data Preprocessing

The dataset was loaded using Pandas.

Missing values were checked.

The target variable was separated from the input features.

The dataset was divided into 80% training data and 20% testing data.

StandardScaler was used for feature scaling.

## Machine Learning Model

Algorithm: Logistic Regression

## Model Evaluation

Accuracy Score:

REPLACE_WITH_YOUR_ACCURACY

## Model Serialization

The trained model was saved as:

model.pkl

## Flask API

The Flask application loads the trained model and accepts patient information in JSON format.

### Home Endpoint

GET /

### Prediction Endpoint

POST /predict

## Example Input

{
    "age": 55,
    "sex": 1,
    "cp": 1,
    "trestbps": 140,
    "chol": 250,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.0,
    "slope": 2,
    "ca": 0,
    "thal": 2
}

## Example Output

{
    "prediction": "Heart Disease Detected"
}

## Project Structure

HeartDiseaseDeployment/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
├── train_model.py
└── heart.csv

## Deployment

The Flask application is deployed using Render.

Render URL:

REPLACE_WITH_YOUR_RENDER_URL

## GitHub Repository

GitHub URL:

REPLACE_WITH_YOUR_GITHUB_URL

## Conclusion

This project demonstrates the complete machine learning deployment process. A Logistic Regression model was trained using the Heart Disease Dataset and evaluated using accuracy score. The trained model was saved using Joblib and integrated into a Flask REST API. The API accepts patient information in JSON format and returns a heart disease prediction. During deployment, challenges included managing Python dependencies, preparing the required project files, loading the saved model correctly, and configuring the Flask application for cloud deployment. MLOps is important because it connects machine learning development with version control, testing, packaging, deployment, and maintenance. GitHub helps manage the source code, while Render provides cloud deployment for the Flask application.
