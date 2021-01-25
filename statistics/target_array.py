from sklearn.datasets import load_diabetes
from random import choice
from random import seed
import numpy as np
# seed(1)
# Do not change the code below

# print(diabetes.shape)
# diabetes_fulldata = np.hstack((diabetes, np.zeros((diabetes.shape[0],1))))

# print(diabetes_fulldata)

# x_miss_idx = [choice(range(diabetes.shape[0])) for _ in range(10)]
# y_miss_idx = [choice(range(diabetes.shape[1])) for _ in range(10)]

# for x, y in zip(x_miss_idx, y_miss_idx):
#     diabetes[x,y] = np.nan

# dbts_rmv_nan = diabetes[~np.isnan(diabetes).any(1)]
# print(dbts_rmv_nan)

diabetes = load_diabetes()['data']
target_arr = load_diabetes()['target']
diabetes_fulldata = np.concatenate((diabetes, target_arr.reshape(-1,1)), axis=1)
# print(target_arr.shape)
# print(target_arr)
# print(target_arr.reshape(-1,1))
# print(target_arr.shape)
print(diabetes_fulldata)
