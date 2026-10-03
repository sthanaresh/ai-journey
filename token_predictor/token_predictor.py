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

    def is_overfitting(
        self, X_train, y_train, X_test, y_test, threshold: float = 0.15
    ) -> bool:
        train_predict = self.model.predict(X_train)
        train_r2 = r2_score(y_train, train_predict)
        test_predict = self.model.predict(X_test)
        test_r2 = r2_score(y_test, test_predict)
        return train_r2 - test_r2 > threshold


X = np.array([[10], [20], [30], [40], [50], [60], [70]])
y = np.array([13, 27, 39, 53, 65, 79, 91])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

predictor = TokenPredictor()
predictor.fit(X_train, y_train)
print(predictor.evaluate(X_test, y_test))

result = predictor.predict(100)
print(f"For 100 words, predicted token is: {result}")

# Add a method is_overfitting(self, X_train, y_train, X_test, y_test, threshold: float = 0.15) -> bool that computes R²
# on both train and test sets, and returns True if train_r2 - test_r2 > threshold (a simple, real heuristic for detecting overfitting)
# Test it with a case that should return True and one that should return False


# true case:
X_train_1 = np.array([[1], [2], [3], [4], [5]])

y_train_1 = np.array([1, 2, 3, 4, 5])

X_test_1 = np.array([[6], [7], [8]])

# Very different from the learned relationship
y_test_1 = np.array([100, 200, 300])

predictor_1 = TokenPredictor()
predictor_1.fit(X_train_1, y_train_1)

print(predictor_1.is_overfitting(X_train_1, y_train_1, X_test_1, y_test_1))

# false case:
X_train_2 = np.array([[10], [20], [30], [40], [50]])

y_train_2 = np.array([13, 27, 39, 53, 65])

X_test_2 = np.array([[60], [70]])

y_test_2 = np.array([79, 91])

predictor_2 = TokenPredictor()
predictor_2.fit(X_train_2, y_train_2)

print(predictor_2.is_overfitting(X_train_2, y_train_2, X_test_2, y_test_2))
