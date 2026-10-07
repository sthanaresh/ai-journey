from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split


class ModelEvaluator:
    def __init__(self, model):
        # store the trained model
        self.model = model

    def evaluate(self, X_test, y_test) -> dict:
        # return {"accuracy": ..., "precision": ..., "recall": ..., "confusion_matrix": ...}
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)
        cm = confusion_matrix(y_test, predictions)
        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "confusion_matrix": cm,
        }

    def report(self, X_test, y_test) -> None:
        # pretty-print the evaluation results, labeled clearly
        results = self.evaluate(X_test, y_test)

        print(f"Accuracy:                 {results['accuracy']:.3f}")
        print(f"Precision:                 {results['precision']:.3f}")
        print(f"Recall:                 {results['recall']:.3f}")
        print(f"Confusion Matrix:                 {results['confusion_matrix']}")


data = load_breast_cancer()
X, y = data.data, data.target

# Train the original model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
original_model = LogisticRegression(max_iter=5000)
original_model.fit(X_train, y_train)

# Train the weak model
weak_model = LogisticRegression(max_iter=5000)
weak_model.fit(X_train[:20], y_train[:20])


original_evaluator = ModelEvaluator(original_model)
weak_evaluator = ModelEvaluator(weak_model)

print()
print("=" * 40)
print("ORIGINAL MODEL")
print("=" * 40)
original_evaluator.report(X_test, y_test)

print()
print("=" * 40)
print("WEAK MODEL")
print("=" * 40)
weak_evaluator.report(X_test, y_test)
