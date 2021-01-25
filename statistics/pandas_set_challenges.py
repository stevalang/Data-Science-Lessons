import pandas as pd
import numpy as np
import random
# lst = list('This is a list that is made from a string!')

# Your code below
# lst_to_series = pd.Series(lst)

# print(lst_to_series)

# lst = list('This is a list that is made from a string!')
# arr = np.arange(42)
# d = dict(zip(lst, arr))

# # Your code below
# dict_to_series = pd.Series(d)
# print(dict_to_series)

# lst_to_ser = pd.Series(list('This is a list that is made from a string!'))
# arr_to_ser = pd.Series(np.arange(42))

# Your code below
# df = pd.DataFrame({'col1': lst_to_ser, 'col2': arr_to_ser})
# print(df)
# Create a series
# prices = pd.Series([1,1,2,3,5],
#                    index=['apple', 'pear', 'banana', 'mango', 'jackfruit'])

# print(prices)
# print(prices.index)

# numeric_labeled = pd.Series(range(10,50,10), index=range(3,7))

# print(numeric_labeled, '\n')

# Will this return the item at position 3 or with label 3?
# print(numeric_labeled[3])

# Use .iloc to be sure the desired series is being returned
# print(numeric_labeled.iloc[3])
# ser = pd.Series(['1915-06-06T12:37', '21 Mar 2013', '1972-05-05', '04-07-2011', '20120205', '1972-05-05', '2019/03/01'])
# ser_ = pd.DataFrame(ser)
# dt_ser = pd.to_datetime(ser_[0])
# print(dt_ser)




# Don't alter the code below
random.seed(1)
cities = pd.Series([random.choice(['Denver', 'NYC', 'Chicago']) for _ in range(50)])
temps = pd.Series(np.random.uniform(low=35, high=75, size=50))

# Your code below
df = pd.DataFrame({"cities": cities, "temps": temps})
grouped_cities = df.mean().groupby('cities')
print(grouped_cities.mean())