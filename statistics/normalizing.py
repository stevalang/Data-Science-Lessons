from sklearn.datasets import load_iris
import numpy as np

iris_data = load_iris()['data']

# You code below
# print(iris_data)
# print(iris_data[5])

# col1 = iris_data[:, 0]
# col2 = iris_data[:, 1]
# col3 = iris_data[:, 2]
# col4 = iris_data[:, 3]

# col1 = np.round((col1 - min(col1)) / (max(col1) - min(col1)), 2)
# col2 = np.round((col2 - min(col2)) / (max(col2) - min(col2)), 2)
# col3 = np.round((col3 - min(col3)) / (max(col3) - min(col3)), 2)
# col4 = np.round((col4 - min(col4)) / (max(col4) - min(col4)), 2)


# matrix = np.array([col1, col2, col3, col4]).transpose()

# print(matrix)

min_ = np.min(iris_data, axis=0)
max_ = np.max(iris_data, axis=0)
iris_data_normalized = np.round((iris_data - min_) / (max_ - min_),2)

ptp = np.ptp(iris_data, axis=0)
# print(np.round(ptp,2))
# print(iris_data_normalized)
print(np.random.random((30,1)))