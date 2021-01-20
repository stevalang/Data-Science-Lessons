# import numpy as np

# def elements_twice_min(arr):
#     """
#     Return all elements of array arr that are greater than or equal to 2 times
#     the minimum element of arr.

#     Parameters
#     ----------
#     arr: numpy array (n, m)

#     Returns
#     -------
#     numpy Array, a vector of size between: 0 and (n * m)
#     """
    

#     return arr[arr >= 2 * np.min(arr)]

# arr = np.arange(12)
# print(elements_twice_min(arr))

import numpy as np

def mat_addition(A, B):
    """
    Add vector/matrix arrays A and B together. If they cannot be added
    return False.

    Parameters
    ----------
    A: numpy array size of (n,) or (n, m)
    B: numpy array size of (p,) or (p, q)

    Returns
    -------
    numpy Array of same size as A and B, or False if their sizes differ.
    """
 
    for i in range(A.shape[0]):
        if A.shape[i]== B.shape[i]:
            return A + B
        else:
            return False


a = np.array([7, 2, 9])
b = np.array([3, 1, 7])
print(mat_addition(a, b))c