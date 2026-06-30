import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/smartphone_battery_drain_dataset.csv")

sns.scatterplot(
    x="Screen_On_Time_min",
    y="Battery_Drop_Per_Hour",
    data=df
)

plt.title("Screen_On_Time_min vs Battery_Drop_Per_Hour")
plt.xlabel("Screen_On_Time_min")
plt.ylabel("Battery_Drop_Per_Hour")

plt.show()