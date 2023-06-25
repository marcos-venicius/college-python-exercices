#!/usr/bin/env python3

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# Loads dataset
iris_dataset = load_iris()

characteristics = iris_dataset.data

groups = KMeans(n_clusters=3)
groups.fit(X=characteristics)
labels = groups.labels_

fig1 = plt.figure(1)
ax = fig1.add_subplot(projection='3d')
ax.set_xlabel('Comprimento Sépala')
ax.set_ylabel('Largura Sépala')
ax.set_zlabel('Comprimento Pétala')
ax.scatter(characteristics[:, 0], characteristics[:, 1], characteristics[:, 2], c=labels, edgecolor='k')

target = iris_dataset.target
fig2 = plt.figure(2)
ax = fig2.add_subplot(projection='3d')
ax.set_xlabel('Comprimento Sépala')
ax.set_ylabel('Largura Sépala')
ax.set_zlabel('Comprimento Pétala')
ax.scatter(characteristics[:, 0], characteristics[:, 1], characteristics[:, 2], c=target, edgecolor='k')

plt.show()
