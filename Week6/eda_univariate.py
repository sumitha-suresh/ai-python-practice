import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = pd.DataFrame({
    "Age": [22, 25, 29, 24, 35, 45, 52, 23, 26, 28, 30, 40]
})

print("Univariate Analysis (Age):")
print(data["Age"].describe())

# Histogram
sns.histplot(data["Age"], bins=5, kde=True)
plt.title("Univariate Analysis - Age Distribution")
plt.show()