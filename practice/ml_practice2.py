# Using this data (imagine it's real: prompt length in words → tokens used):
# X = np.array([[10], [20], [30], [40], [50]])  # words
# y = np.array([13, 27, 39, 53, 65])  # tokens (not perfectly linear this time)

# Fit a LinearRegression model
# Print coef_ and intercept_
# Predict tokens for a 35-word prompt

# Compute the model's predictions on the original X data (the training data itself), and manually compare them
# to the real y values — are they exactly equal, or slightly off? Why might that be, given the data isn't perfectly
# linear this time?


import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[10], [20], [30], [40], [50]])
y = np.array([13, 27, 39, 53, 65])

model = LinearRegression()
model.fit(X, y)
print(f"Coefficient: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# Tokens for 35-word
tokens = model.predict([[35]])
print(f"Tokens: {tokens}")

# Model's prediction on the original X data
predictions = model.predict(X)
print(f"Predictions: {predictions}")
print(f"Actual: {y}")

# MSE(Mean Squared Error) Calculation
MSE = (
    (13 - 13.4) ** 2
    + (27 - 26.4) ** 2
    + (39 - 39.4) ** 2
    + (53 - 52.4) ** 2
    + (65 - 65.4) ** 2
) / 5
print(f"MSE: {MSE}")
