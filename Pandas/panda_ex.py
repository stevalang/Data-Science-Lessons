import pandas as pd
import numpy as np

grocery = pd.DataFrame({'category':['produce', 'produce', 'meat',
                                    'meat', 'meat', 'cheese', 'cheese'],
                        'item':['celery', 'apple', 'ham', 'turkey',  'lamb',
                                'cheddar', 'brie'],
                        'price':[.99, .49, 1.89, 4.34, 9.50, 6.25, 8.0]})






# for name, category in grouped_grocery:
#     print(name)
#     print(category)



# grouped_grocery.filter(lambda x: x < 3)
grouped_grocery = grocery.groupby('category')
one_mean = grouped_grocery.filter(lambda x: x.mean() > 3)

two_max = grouped_grocery.aggregate(max)

three_round = grouped_grocery['price'].transform(lambda x: x * .9 if x.max() > 3 else x)
print(three_round)
