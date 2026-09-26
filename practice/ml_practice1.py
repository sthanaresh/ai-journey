# Simple example: predicting cost from tokens used

import numpy as np
from sklearn.linear_model import LinearRegression

# tokens_used -> cost_usd (imagine this is real API usage data)
X = np.array([[100], [200], [300], [400], [500]])  # tokens (must be 2D for sklearn)
y = np.array([0.002, 0.004, 0.006, 0.008, 0.010])  # cost

model = LinearRegression()
model.fit(X, y)

print(model.coef_)
print(model.intercept_)
new_tokens = np.array([[250], [600]])
predictions = model.predict(new_tokens)
print(predictions)
