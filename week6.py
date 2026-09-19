import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

parameters = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [2, 3, 4, 5]
}

grid = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    parameters,
    cv=5
)

grid.fit(X_train, y_train)

print("\nBest Parameters:")
print(grid.best_params_)

print("Best CV Accuracy:", grid.best_score_)

best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)

print("Test Accuracy:", accuracy_score(y_test, y_pred))

plt.figure(figsize=(7, 5))

plot_tree(
    best_model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.title("Best Decision Tree")

plt.show()
