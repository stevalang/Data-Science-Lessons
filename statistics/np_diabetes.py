# from sklearn.datasets import load_diabetes
# from random import choice
# from random import seed
# import numpy as np

# seed(1)
# diabetes = load_diabetes()['data']
# print(diabetes.shape)
# x_miss_idx = [choice(range(diabetes.shape[0])) for _ in range(10)]
# y_miss_idx = [choice(range(diabetes.shape[1])) for _ in range(10)]

# for x, y in zip(x_miss_idx, y_miss_idx):
#     diabetes[x, y] = np.nan
# dbts_rmv_nan = np.array()
# np.any(diabetes, axis=1,out=dbts_rmv_nan, ~ np.isnan()  )

# Imports
from sklearn.datasets import load_diabetes
from random import choice
from random import seed
import numpy as np

# Do not change the code below
# seed(1)
# diabetes = load_diabetes()['data']
# x_miss_idx = [choice(range(diabetes.shape[0])) for _ in range(10)]
# y_miss_idx = [choice(range(diabetes.shape[1])) for _ in range(10)]

# for x, y in zip(x_miss_idx, y_miss_idx):
#     diabetes[x,y] = np.nan

# Your code below, the data is in the variable 'diabetes'
# print(~np.isnan(diabetes).any(1))
# dbts_rmv_nan = diabetes[~np.isnan(diabetes).any(0)]

# print(dbts_rmv_nan)

diabetes = load_diabetes()['data']
target = np.a([])
diabetes_fulldata = np.vstack([diabetes['data'], target])
# print(diabetes_fulldata)
print(load_diabetes()['DESCR'])