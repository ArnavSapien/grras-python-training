import joblib
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

model = joblib.load("model.joblib")

@app.post("/predict")
def predict(data: dict):
    input_data = pd.DataFrame([{
        "Hours Studied": data["hours_studied"],
        "Previous Scores": data["previous_scores"],
        "Extracurricular Activities": data["extracurricular_activities"],
        "Sleep Hours": data["sleep_hours"],
        "Sample Question Papers Practiced": data["sample_question_papers_practiced"]
    }])

    prediction = model.predict(input_data)

    return {
        "predicted_performance_index": round(prediction[0], 2)
    }