# Imports
import sklearn
from sklearn.datasets import load_iris

# Read in data set

iris_dataset = load_iris()
iris_vectors = iris_dataset['data']

# # Find the average iris
avg_irirs = iris_vectors.mean(axis=0)

# print(iris_dataset['DESCR'])
# print(iris_vectors)

# print(iris_vectors[:5])

# from oop import avg

# import random

# lst = [random.randint(0, 10) for _ in range(10)]

# print(avg(lst))