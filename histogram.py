import pandas as pd
import matplotlib.pyplot as plt

# Sample data (You can replace with your dataset)
data = {
    "Age": [18, 22, 25, 19, 30, 35, 40, 28, 21, 23, 27, 29, 31, 33, 36]
}

df = pd.DataFrame(data)

# Create Histogram
plt.hist(df["Age"], bins=5)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()