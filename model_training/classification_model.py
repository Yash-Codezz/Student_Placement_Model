# === Importing Libraries ==============================

import pandas as pd

from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import StackingClassifier, RandomForestClassifier

import joblib


# === Imporitng Dataset ==============================

data = pd.read_csv('data/student_placement_synthetic.csv')

data.drop(columns=['extracurriculars', 'salary_package_lpa'], inplace=True)


# === Preprocessing ==============================

preprocessing = ColumnTransformer(transformers=[
    ('ordianl', OrdinalEncoder(categories=[['Tier-1', 'Tier-2', 'Tier-3']]), ['college_tier']),
    ('ohe', OneHotEncoder(drop='first', handle_unknown='ignore'), ['branch'])    
], remainder='passthrough')


# === Model Pipeline ==============================

base_models = [
    ('lr', LogisticRegression(C=0.01)),
    ('knn', KNeighborsClassifier(n_neighbors=18, weights='distance')),
    ('rf', RandomForestClassifier(n_estimators=900, criterion='gini', max_depth=8, max_features='sqrt', class_weight=None))
]

meta_model = LogisticRegression()


model = Pipeline(steps=[
    ('preprocessing', preprocessing),
    ('scaler', StandardScaler()),
    ('model', StackingClassifier(estimators=base_models, final_estimator=meta_model, cv=5))
])


# === Data Splitting ==============================

X = data.drop(columns=['placement_status'])
y = data['placement_status']


# === Model Training ==============================

model.fit(X, y)

print("Model Trained Successfully!")


# === Saving Model ==============================

joblib.dump(model, 'model/JobPredictor.pkl')

print('Model Saved Successfully')