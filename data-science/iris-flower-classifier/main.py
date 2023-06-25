#!/usr/bin/env python3

from sklearn.datasets import load_iris, fetch_kddcup99
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.svm import SVC


# Loads dataset
iris_dataset = load_iris()

characteristics = iris_dataset.data
labels = iris_dataset.target

# Split the data in chunks to each type of action
characteristics_train, characteristics_test, labels_train, labels_test = train_test_split(characteristics, labels)

# Create decision tree classifier with max depth of 2 levels
tree = DecisionTreeClassifier(max_depth=2)

# Train the classifier
tree.fit(X=characteristics_train, y=labels_train)

# Predict data labels with the trained decision tree classifier
labels_predicted = tree.predict(characteristics_test)

# Calculate accuracy of the predicted labels with real data
accuracy_tree = accuracy_score(labels_test, labels_predicted)

# Create a Support Vector Classifier
clf = SVC()
# Train the SVC with train data
clf.fit(X=characteristics_train, y=labels_train)

# Predict labels
labels_predicted_svm = clf.predict(characteristics_test)

# Calculate accuracy of the predicted labels with real data
accuracy_svm = accuracy_score(labels_test, labels_predicted_svm)

# Calculate precision on trained models
accuracy_tree_percentage = round(accuracy_tree * 100, 2)
accuracy_svm_percentage = round(accuracy_svm * 100, 2)

print(f"Decision tree accuracy: {accuracy_tree_percentage}%")
print(f"SVM accuracy: {accuracy_svm_percentage}%")
print()

tree_structure = export_text(tree, feature_names=iris_dataset['feature_names'])

print('Tree structure')
print(tree_structure)
