# === Importing Libraries ==============================

from fastapi import FastAPI


# === FastAPI Object ==============================

app = FastAPI()


# === Home Endpont ==============================

@app.get("/")
def Home():

    return {'message' : 'Student Placement Model API'}