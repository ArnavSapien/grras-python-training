import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.read_csv("dataset/smartphone_battery_drain_dataset.csv")

df.dropna(inplace=True)

# Clean text columns
df["Network_Type"] = df["Network_Type"].str.lower().str.strip()
df["Charging_State"] = df["Charging_State"].str.lower().str.strip()

# Encode Network_Type
network_encoder = LabelEncoder()
df["Network_Type"] = network_encoder.fit_transform(df["Network_Type"])

# Encode Charging_State
df["Charging_State"] = df["Charging_State"].map({
    "charging": 1,
    "not charging": 0
})

# Check if mapping created any NaN
print(df["Charging_State"].isnull().sum())

feature_columns = [
    "Screen_On_Time_min",
    "CPU_Usage_%",
    "Battery_Temperature_C",
    "Network_Type",
    "Brightness_Level_%",
    "Charging_State"
]

target_column = "Battery_Drop_Per_Hour"

X = df[feature_columns]
y = df[target_column]

# Polynomial conversion
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Save model properly
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

# Save polynomial transformer
with open("poly.pkl", "wb") as file:
    pickle.dump(poly, file)

# Save network encoder
with open("network_encoder.pkl", "wb") as file:
    pickle.dump(network_encoder, file)