import numpy as np

matrix_A = np.array([[3, 5], [1, 7]])
matrix_B = np.array([[2, 11], [1, 4]])

A_times_B = np.dot(matrix_A, matrix_B)
B_times_A = np.dot(matrix_B, matrix_A)

# print(f'AB=\n{A_times_B}\n')
# print(f'BA =\n{B_times_A}')


# --------------------------------------------

v = np.arange(2, 9, 2)
w = np.array([1, 3, 4, 9])

v_dot_w = np.dot(v, w)

# Alternatively call the method using a vector as a calling object

w_dot_v = v.dot(w)

print(f'v * w = {v_dot_w}')
print(f'w * v = {w_dot_v}')


