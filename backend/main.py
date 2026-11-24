# === Importing Libraries ==============================

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from schema.student_info import StudentInfo

from model.model_prediction import model_prediction


# === FastAPI Object ==============================

app = FastAPI()


# === Home Endpont ==============================

@app.get("/")
def Home():

    return {'message' : 'Student Placement Model API'}


# === Predict Endpoint ==============================

@app.post("/predict")
def predict(info: StudentInfo):

    try:

        student_info = info.model_dump()

        prediction = model_prediction(student_info)

        return JSONResponse(status_code=200, content={'response' : prediction})

    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))