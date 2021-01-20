import numpy as np

# # establish a
# a = np.array([[3, 1], [0, 2]])


# print(array([3, 0])) # check v1
# print(a.dot(np.array([[3,1], [0, 2]])))
# # check v2
# a.dot(np.array([np.sqrt(3)/2, 0.5]))
# #looks like 3 times v1, so v1 is in


# >>> import numpy as np
# >>> a = np.array([[3,1], [0,2]])  # establish a
# >>> a.dot(np.array([1,0]))  # check v1
# array([3, 0])  # looks like 3 times v1, so v1 is in
# >>> a.dot(np.array([np.sqrt(3)/2, 0.5]))  # check v2
# array([3.09807621, 1.        ])  # ok, so 1 is clearly twice 0.5, so is 3.098 twice sqrt(3)/2?
# >>> np.sqrt(3)
# 1.7320508075688772  # guess not! v2 is out
# >>> a.dot(np.array([-np.sqrt(2)/2, np.sqrt(2)/2]))  # check v3
# array([-1.41421356,  1.41421356])  # still symmetric values where the first one is negative, so there exists some scalar for this vector that works as lambda, so this is an eigenvector; v3 is in
# #  So, v1 and v3 are in, v2 is out.

print(-1.41421356 / (-np.sqrt(2) / 2))