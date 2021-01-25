import pandas as pd
import numpy as np

grocery = pd.DataFrame({'category':['produce', 'produce', 'meat',
                                    'meat', 'meat', 'cheese', 'cheese'],
                        'item':['celery', 'apple', 'ham', 'turkey',  'lamb',
                                'cheddar', 'brie'],
                        'price':[.99, .49, 1.89, 4.34, 9.50, 6.25, 8.0]})




grouped_grocery = grocery.groupby('category')

# for name, category in grouped_grocery:
#     print(name)
#     print(category)



# grouped_grocery.filter(lambda x: x < 3)
a = grouped_grocery.filter(lambda x: x.mean() < 3)
one_mean = a.drop(a, axis=1)

two_max = grouped_grocery.max()
# grouped_grocery['new_price'].transform(lambda x: x * .9 if grouped_grocery['category'].max() > 3)
three_round = grocery['price'].transform(lambda x: x*.9 if x > 3 else x)
'''
Perform the following operations using split-apply-combine.
Remove all items in categories where the mean price in that category is less than $3.00.
Find the maximum values in each category for all features. 
(What does Pandas take to be the maximum value of the 'item' column?)
If the maximum price in a category is more than $3.00, reduce all prices in that 
category by 10%. Return a Series of the new price column.
'''
print('\n')
print(one_mean)
print('\n')
print(two_max)
print('\n')
print(three_round)
