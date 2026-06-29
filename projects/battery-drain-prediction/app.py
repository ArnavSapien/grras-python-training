import pickle
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Load polynomial transformer
with open("poly.pkl", "rb") as file:
    poly = pickle.load(file)

# Load saved encoder
with open("network_encoder.pkl", "rb") as file:
    network_encoder = pickle.load(file)


@app.post("/predict")
def predict(data: dict):

    input_data = pd.DataFrame([{
        "Screen_On_Time_min": data["Screen_On_Time_min"],
        "CPU_Usage_%": data["CPU_Usage_%"],
        "Battery_Temperature_C": data["Battery_Temperature_C"],
        "Network_Type": data["Network_Type"],
        "Brightness_Level_%": data["Brightness_Level_%"],
        "Charging_State": data["Charging_State"]
    }])

    # Clean and encode Network_Type
    input_data["Network_Type"] = input_data["Network_Type"].str.lower().str.strip()
    input_data["Network_Type"] = network_encoder.transform(input_data["Network_Type"])

    # Convert input into polynomial features
    input_poly = poly.transform(input_data)

    # Predict
    prediction = model.predict(input_poly)

    return {
        "Battery_Drop_Per_Hour": round(prediction[0], 2)
    }