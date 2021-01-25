import pandas as pd
import numpy as np

grocery = pd.DataFrame({'category':['produce', 'produce', 'meat',
                                    'meat', 'meat', 'cheese', 'cheese'],
                        'item':['celery', 'apple', 'ham', 'turkey',  'lamb',
                                'cheddar', 'brie'],
                        'price':[.99, .49, 1.89, 4.34, 9.50, 6.25, 8.0]})
print(grocery)

one_mean = 0

two_max = 0

three_round = 0