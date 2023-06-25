# Iris classification using Decision Tree Classifier & Support Vector Classifier

This code loads the iris dataset and trains on that data so that the AI is able to correctly determine which is a given iris.

## Data resolution

- 0 -> Iris Setosa
- 1 -> Iris Versicolor
- 2 -> Iris Virginica

## Installing dependencies

```shell
pip install -r ./requirements.txt
```

## Running

```shell
./main.py
```

## Output example

```
Decision tree accuracy: 94.74%
SVM accuracy: 92.11%

Tree structure
|--- petal width (cm) <= 0.70
|   |--- class: 0
|--- petal width (cm) >  0.70
|   |--- petal width (cm) <= 1.75
|   |   |--- class: 1
|   |--- petal width (cm) >  1.75
|   |   |--- class: 2
```
