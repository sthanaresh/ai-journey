# A real, built-in dataset
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X, y = data.data, data.target

print(X.shape)
print(y[:10])
print(data.target_names)
print(
    "*******************************************************************************************************************"
)
# Train the classifier
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions[:10])
print(y_test[:10])
print(
    "******************************************************************************************************"
)

# compute accuracy, precision, and recall
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"Confusion Matrix: {cm}")
