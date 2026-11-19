# === Importing Libraries ==============================

import pandas as pd

from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import StackingRegressor, RandomForestRegressor

import joblib


# === Imporitng Dataset ==============================

data = pd.read_csv('data/student_placement_synthetic.csv')

data.drop(columns=['extracurriculars', 'placement_status'], inplace=True)

data.dropna(subset='salary_package_lpa', inplace=True)


# === Preprocessing ==============================

preprocessing = ColumnTransformer(transformers=[
    ('ordianl', OrdinalEncoder(categories=[['Tier-1', 'Tier-2', 'Tier-3']]), ['college_tier']),
    ('ohe', OneHotEncoder(drop='first', handle_unknown='ignore'), ['branch'])    
], remainder='passthrough')


# === Model Pipeline ==============================

base_models = [
    ('ridge', Ridge(alpha=10)),
    ('knn', KNeighborsRegressor(n_neighbors=13)),
    ('rf', RandomForestRegressor(n_estimators=400, max_depth=18, max_features=None))
]

meta_model = LinearRegression()


model = Pipeline(steps=[
    ('preprocessing', preprocessing),
    ('scaler', StandardScaler()),
    ('model', StackingRegressor(estimators=base_models, final_estimator=meta_model, cv=5))
])


# === Data Splitting ==============================

X = data.drop(columns=['salary_package_lpa'])
y = data['salary_package_lpa']


# === Model Training ==============================

model.fit(X, y)

print("Model Trained Successfully!")


# === Saving Model ==============================

joblib.dump(model, 'model/PayPredictor.pkl')

print('Model Saved Successfully')