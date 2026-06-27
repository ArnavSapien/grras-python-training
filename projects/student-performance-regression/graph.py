import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/Student_Performance.csv")

sns.scatterplot(
    x="Hours Studied",
    y="Performance Index",
    data=df
)

plt.title("Hours Studied vs Performance Index")
plt.xlabel("Hours Studied")
plt.ylabel("Performance Index")

plt.show()
plt.savefig("hours_vs_performance.png")