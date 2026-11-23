# === Importing Libraries ==============================

import os

import joblib

import pandas as pd


# === Loading Model ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

REG_MODEL_PATH = os.path.join(BASE_DIR, 'model/PayPredictor.pkl')

CLS_MODEL_PATH = os.path.join(BASE_DIR, 'model/JobPredictor.pkl')

reg_model = joblib.load(REG_MODEL_PATH)

cls_model = joblib.load(CLS_MODEL_PATH)


# === Model Prediction ==============================

def model_prediction(student_info: dict):

    # Student Placement Prediction
    info = pd.DataFrame([student_info])

    placement_prediction = cls_model.predict(info)

    if(placement_prediction == 1):

        # Student Expected Salary
        income_prediction = reg_model.predict(info)

        return f"Yes!, Expected Salary: {income_prediction[0]:.2f} L.P.A"
    else:

        return 'No!'