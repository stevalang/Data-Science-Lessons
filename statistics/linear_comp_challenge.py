import pandas as pd
import numpy as np
from scipy import spatial

# p = np.array([[8, -3, 8, 5, -5]])
# q = np.array([[-4, 8, 7, -1, 6]])

# a = print(np.dot(p, q, out=None) / (np.linalg.norm(p) * np.linalg.norm(q)))


# def format_matrix_string(mat):
#     """
#     Convert a NumPy matrix/array to a string where rows are separated by the
#     newline character '\n'.
#     INPUT: mat: NumPy array
#     OUTPUT: str
#     """
#     rowstrs = [', '.join(row) for row in np.round(mat, 2).astype(str)]
#     return ' \n '.join(rowstrs)



# B = np.array([[ -5,  3, -1], [-3, 6,  -1], [-1, -7, 3]])
# B_inv = np.linalg.inv(B)
# print(B_inv.dot(np.array([[-10], [18], [-38]])))


# p_dot_q = np.dot(p, q)
# print(p_dot_q)

# dist = np.linalg.norm(p - q)
# # print(dist)

# cos_sim = np.dot(p, q) / (norm(p) * norm(q))
# print(cos_sim)

# def dot(A,B):
#     return (sum(a*b for a,b in zip(A,B)))

# def cosine_similarity(a,b):
#     return dot(a,b) / ( (dot(a,a) **.5) * (dot(b,b) ** .5) )



# p = np.array([[8], [-3], [8], [5], [-5]])
# q = np.array([[-4], [8], [7], [-1], [6]])


# print(cosine_similarity(p,q))

# def get_cosine(text1, text2):
#   vec1 = text1
#   vec2 = text2
#   intersection = set(vec1.keys()) & set(vec2.keys())
#   numerator = sum([vec1[x] * vec2[x] for x in intersection])
#   sum1 = sum([vec1[x]**2 for x in vec1.keys()])
#   sum2 = sum([vec2[x]**2 for x in vec2.keys()])
#   denominator = math.sqrt(sum1) * math.sqrt(sum2)
#   if not denominator:
#      return 0.0
#   else:
#      return round(float(numerator) / denominator, 3)
# dataSet1 = [3, 45, 7, 2]
# dataSet2 = [2, 54, 13, 15]
# get_cosine(dataSet1, dataSet2)

# p = np.array([[8, -3, 8, 5, -5]])
# q = np.array([[-4, 8, 7, -1, 6]])

# print(get_cosine(p,q))

A = np.array([[3, 0], [0, 2]])
v1 = np.array([-(2**.5)/2 , (2**.5)/2])

a_dot_v1 = A.dot(v1)
print(a_dot_v1)