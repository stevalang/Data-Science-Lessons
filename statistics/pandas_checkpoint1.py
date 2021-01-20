import pandas as pd
import matplotlib as mpl
import numpy as np

# def df_histogram(df, colname, num_bins = 10):
#     return df.plot()




# A = np.array([[2, 8], [3, 1]])
# B = np.array([[0, 1], [1, 1]])
# a_dot_b = np.dot(A, B)
# print(a_dot_b)

S = np.array([[2, 8], [3, 1]])
T = np.array([[0, 1], [1, 1]])
S_t = S.transpose()
S_t_dot_T = S_t.dot(T)
print(S_t_dot_T)
