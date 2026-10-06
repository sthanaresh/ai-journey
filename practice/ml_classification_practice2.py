# Using the same X_train/X_test/y_train/y_test as before, train a second model but artificially make it worse by
# using way less training data — just the first 20 rows.
# Compute accuracy, precision, and recall for this weaker model and compare to the original.

# A real, built-in dataset
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X, y = data.data, data.target

# Train the original model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
original_model = LogisticRegression(max_iter=5000)
original_model.fit(X_train, y_train)
original_predictions = original_model.predict(X_test)

# Compute accuracy, precision, and recall for original model
accuracy = accuracy_score(y_test, original_predictions)
precision = precision_score(y_test, original_predictions)
recall = recall_score(y_test, original_predictions)

print("\n************************Original Model*************************")
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")

# Train the weak model
weak_model = LogisticRegression(max_iter=5000)
weak_model.fit(X_train[:20], y_train[:20])
weak_predictions = weak_model.predict(X_test)

# Compute accuracy, precision, and recall for the weak model
weak_accuracy = accuracy_score(y_test, weak_predictions)
weak_precision = precision_score(y_test, weak_predictions)
weak_recall = recall_score(y_test, weak_predictions)

print("\n**************************Weak Model****************************")
print(f"Accuracy: {weak_accuracy}")
print(f"Precision: {weak_precision}")
print(f"Recall: {weak_recall}")


# Write a function classification_summary(y_true, y_pred) -> dict that returns {"accuracy": ..., "precision": ...,
# "recall": ...} in one call


def classification_summary(y_true, y_pred) -> dict:
    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
    }


classification = classification_summary(y_test, original_predictions)
print(
    f"****************Using function in original model**********************\n{classification} "
)
