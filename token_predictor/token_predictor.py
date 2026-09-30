import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


class TokenPredictor:
    def __init__(self):
        # initialize a LinearRegression model
        self.model = LinearRegression()

    def fit(self, X, y) -> None:
        # train the model
        self.model.fit(X, y)

    def predict(self, words: int) -> float:
        # predict tokens for a single word count (remember: needs 2D input)
        prediction = self.model.predict([[words]])
        return float(prediction[0])

    def evaluate(self, X_test, y_test) -> dict:
        # predict on X_test, compare to y_test
        # return {"mse": ..., "r2": ...}
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        return {"mse": mse, "r2": r2}


X = np.array([[10], [20], [30], [40], [50], [60], [70]])
y = np.array([13, 27, 39, 53, 65, 79, 91])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

predictor = TokenPredictor()
predictor.fit(X_train, y_train)
print(predictor.evaluate(X_test, y_test))
