# Numpy
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot = np.dot(a, b)

print(a + b)
print(a * b)
print(dot)


print(
    "*************************************************************************************************************"
)
# Pandas
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "score": [85, 42, 91, 67],
    "passed": [True, False, True, True],
}

df = pd.DataFrame(data)
print(df)
print(df["score"] >= 70)
passed_students = df[df["score"] >= 70]
print(passed_students)

print(
    "***************************************************************************************************************"
)

# Exercise A (NumPy): Given scores = np.array([88, 92, 79, 65, 95]), write code to:
# Compute the mean
# Compute how many scores are above the mean (hint: boolean array + .sum())

scores = np.array([88, 92, 79, 65, 95])
mean = scores.mean()
print(mean)

above_mean = scores > mean
print(above_mean)

count = above_mean.sum()
print(count)

print(
    "**************************************************************************************************************"
)
# Exercise B (Pandas): Using this data:
data1 = {
    "prompt": ["Q1", "Q2", "Q3", "Q4"],
    "tokens_used": [120, 340, 89, 512],
    "cost_usd": [0.002, 0.006, 0.001, 0.009],
}
# df = pd.DataFrame(data)
# Write code to:
# Filter rows where tokens_used > 100
# Compute the total cost_usd across ALL rows (hint: .sum() on a column)

df1 = pd.DataFrame(data1)
print(df1)

filtered_rows = df1[df1["tokens_used"] > 100]
print(filtered_rows)

total_cost_usd = df1["cost_usd"].sum()
print(total_cost_usd)
