import numpy as np


arr = np.arange(0, 300, 3)
print(arr)
print(arr % 2 == 0)

arr[arr % 2 == 0] = 2

print(arr)


print(data[data[:,0] > 5])

import pandas as pd

prices = pd.Series([1,1,2,3,5],
                    index=[12,13,14,15,0])
print(data.iloc[:5,:])

print(data.loc[:,'sepal_l'])