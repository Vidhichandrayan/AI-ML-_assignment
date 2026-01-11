import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "http://127.0.0.1:8000/scores"
data = requests.get(url).json()

df = pd.DataFrame(data)
df["gender"] = df["gender"].str.capitalize()

# Calculate average per gender
grouped = df.groupby("gender")["average_score"].mean().reset_index()
overall_avg = grouped["average_score"].mean()

print("Overall Average Score:", round(overall_avg, 2))

sns.set_theme(style="whitegrid")
plt.figure(figsize=(9, 6))

sns.barplot(data=grouped, x="gender", y="average_score")

plt.axhline(overall_avg, linestyle="--", label=f"Overall Avg: {overall_avg:.1f}")

plt.title("Average Student Performance by Gender", fontsize=14)
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.legend()
plt.tight_layout()
plt.show()
