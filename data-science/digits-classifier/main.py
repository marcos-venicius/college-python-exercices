#!/usr/bin/env python3

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from random import randint
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()

x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=42)

pipeline = make_pipeline(StandardScaler(), LogisticRegression())

pipeline.fit(x_train, y_train)

index = randint(0, len(x_test))

predicted = pipeline.predict(x_test[index].reshape((1, -1)))
real = y_test[index]

plt.imshow(np.reshape(x_test[index], (8, 8)))
plt.title(f'Prediction: {predicted[0]}, Real: {real}')
plt.axis('off')
plt.show()

