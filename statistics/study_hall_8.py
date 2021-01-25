import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import scipy.stats as stats


# df = pd.DataFrame(load_iris()['data'])
# df.columns = ['sep_w', 'sep_l', 'pet_w', 'pet_l']
# df.plot(y = 'sep_w', kind='hist', bins=10)
# plt.show()
# A = np.arange(9).reshape(3, 3)
# x = np.ones((1,3))
# print(A.dot(x))
# sd = 2.75
# mean_sd = 2.75 / np.sqrt(50)
# print(stats.t.interval(alpha=.95, df=99, loc=39.9, scale=mean_sd))
# instantiate dataframe
# data = load_iris()['data']
# df = pd.DataFrame(data)
# df.index = [f'flower # {num}' for num in range(1, 151)]
# print(df.iloc[:,0])
# print(produce.loc[produce['price'] <=3, :])

# produce =produce.drop(['price', 'inventory'], axis=1, inplace=True)


def add_dictionary(dict1, key, dict2):
    d = dict1.copy()
    d[key] = dict2
    return d
person1 = {'name': 'Homer Simpson', 'role': 'schlub'}
person2 = {'name': 'Mr. Burns', 'role': 'supervisor'}

result = add_dictionary(person1, 'manager', person2)

# print(result)
#    {'name': 'Homer Simpson',
#     'role': 'schlub',
#     'manager': {'name': 'Mr. Burns', role: 'supervisor'}}

def remove_gt(n, dct):

    d = dct.copy()

    for k, v in dct.items():
        print(f'{k}:{v}')
        if isinstance(v, (float, int)):
            if v > n:
                del k
    return d

inp = {'a': 8, 'b': 2, 'c': 'montana'}

remove_gt(5, inp)
print(inp) # --> {'b': 2, 'c': 'montana'}