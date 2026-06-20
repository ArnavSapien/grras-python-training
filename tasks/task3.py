# Libraries used: NumPy, Pandas, Matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\grras-python-training\datasets\ecom_data.csv")


print("First 5 rows of data:")
print(df.head())

print("\nMissing values before cleaning:")
print(df.isnull().sum())

df.dropna(subset=["CustomerID", "Description"], inplace=True)

df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["Total_Amount"] = df["Quantity"] * df["UnitPrice"]

df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

average_amount = np.mean(df["Total_Amount"])

df["Sale_Type"] = np.where(
    df["Total_Amount"] >= average_amount,
    "High Sale",
    "Normal Sale"
)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nTotal Sales Amount:", round(df["Total_Amount"].sum(), 2))
print("Average Sale Amount:", round(average_amount, 2))
print("Total Countries:", df["Country"].nunique())
print("Total Customers:", df["CustomerID"].nunique())

top_countries = df.groupby("Country")["Total_Amount"].sum().sort_values(ascending=False).head(5)
top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(5)
monthly_sales = df.groupby("Month")["Total_Amount"].sum()
sale_type_count = df["Sale_Type"].value_counts()

fig, ax = plt.subplots(2, 2, figsize=(14, 10))

# first graph -> bar chart of top countries
ax[0, 0].bar(top_countries.index, top_countries.values)
ax[0, 0].set_title("Top 5 Countries by Sales")
ax[0, 0].set_xlabel("Country")
ax[0, 0].set_ylabel("Total Sales")
ax[0, 0].tick_params(axis="x", rotation=25)

# second graph -> bar chart of top products
ax[0, 1].bar(top_products.index, top_products.values)
ax[0, 1].set_title("Top 5 Products by Quantity")
ax[0, 1].set_xlabel("Product")
ax[0, 1].set_ylabel("Quantity Sold")
ax[0, 1].tick_params(axis="x", rotation=90)

# third graph -> line chart of monthly sales
ax[1, 0].plot(monthly_sales.index, monthly_sales.values, marker="o")
ax[1, 0].set_title("Monthly Sales Trend")
ax[1, 0].set_xlabel("Month")
ax[1, 0].set_ylabel("Total Sales")
ax[1, 0].tick_params(axis="x", rotation=45)
ax[1, 0].grid(True)

# fourth graph -> pie chart of normal sale and high sale
ax[1, 1].pie(
    sale_type_count.values,
    labels=sale_type_count.index,
    autopct="%1.1f%%",
    shadow=True
)
ax[1, 1].set_title("Normal Sale vs High Sale")

plt.show()