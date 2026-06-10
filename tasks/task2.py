import pandas as pd
data = {
        "Emp_ID": [101,102,103,104,105,106],
        "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
        "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
        "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
        "Experinence": [2, 3, 5, 4, 1, 3]
}
df = pd.DataFrame(data)
print(df)
print(df.head(3))
print(df.tail(3))
df.rename(columns={"Name": "Employee Name"}, inplace=True)
print(df)
print(df.info())
print(df.describe())
print(df.shape)