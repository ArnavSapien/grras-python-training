# Battery Drain Prediction using Polynomial Regression

This is a simple Machine Learning project that predicts the **battery drop per hour** of a smartphone based on usage conditions such as screen time, CPU usage, battery temperature, network type, brightness level, and charging state.

The model is trained using **Polynomial Regression** and deployed using **FastAPI**, so predictions can be tested using Swagger UI or Postman.

## Project Overview

The goal of this project is to predict:

```text
Battery_Drop_Per_Hour
```

using the following input features:

```text
Screen_On_Time_min
CPU_Usage_%
Battery_Temperature_C
Network_Type
Brightness_Level_%
Charging_State
```

## Technologies Used

```text
Python
Pandas
Scikit-learn
Polynomial Regression
FastAPI
Uvicorn
Pickle
```

## Project Structure

```text
battery-drain-prediction/
│
├── dataset/
│   └── smartphone_battery_drain_dataset.csv
│
├── train_model.py
├── app.py
├── model.pkl
├── poly.pkl
├── network_encoder.pkl
├── requirements.txt
└── README.md
```

## Dataset Description

The dataset contains smartphone battery usage details. Important columns used in this project are:

| Column Name           | Description                                         |
| --------------------- | --------------------------------------------------- |
| Screen_On_Time_min    | Screen usage time in minutes                        |
| CPU_Usage_%           | CPU usage percentage                                |
| Battery_Temperature_C | Battery temperature in Celsius                      |
| Network_Type          | Type of network such as WiFi, 4G, or 5G             |
| Brightness_Level_%    | Screen brightness percentage                        |
| Charging_State        | Charging status: 1 for Charging, 0 for Not Charging |
| Battery_Drop_Per_Hour | Target value to be predicted                        |

## Model Used

This project uses **Polynomial Regression**.

Polynomial Regression is used because battery drain is not always linear. Battery usage can increase faster when brightness, CPU usage, temperature, and network usage increase together.

The model uses:

```text
PolynomialFeatures
LinearRegression
```

## How to Run the Project

### 1. Create Virtual Environment

```bash
python -m venv myenv
```

Activate it:

```bash
myenv\Scripts\activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python train_model.py
```

This will create:

```text
model.pkl
poly.pkl
network_encoder.pkl
```

### 4. Run FastAPI Server

```bash
uvicorn app:app --reload
```

### 5. Open Swagger UI

Open this URL in browser:

```text
http://127.0.0.1:8000/docs
```

## API Endpoint

```text
POST /predict
```

## Sample Input

```json
{
  "Screen_On_Time_min": 120,
  "CPU_Usage_%": 45,
  "Battery_Temperature_C": 36,
  "Network_Type": "5g",
  "Brightness_Level_%": 70,
  "Charging_State": 0
}
```

## Sample Output

```json
{
  "Battery_Drop_Per_Hour": 12.45
}
```

## Important Note

The model gives an approximate prediction based on the dataset. Real battery drain can also depend on background apps, battery health, device age, operating system, and hardware condition.

## Future Improvements

```text
Add more real-world battery data
Compare Linear Regression and Polynomial Regression
Add model accuracy score
Create a frontend website
Deploy the API online
Add battery life remaining prediction
```

## Conclusion

This project demonstrates how Polynomial Regression can be used to predict smartphone battery drain. It also shows how a trained ML model can be saved using Pickle and used inside a FastAPI backend.