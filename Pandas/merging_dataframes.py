import pandas as pd

# df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
#                     'B': ['B0', 'B1', 'B2', 'B3'],
#                     'C': ['C0', 'C1', 'C2', 'C3'],
#                     'D': ['D0', 'D1', 'D2', 'D3']},
#                     index=[0, 1, 2, 3])

# df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
#                     'B': ['B4', 'B5', 'B6', 'B7'],
#                     'C': ['C4', 'C5', 'C6', 'C7'],
#                     'D': ['D4', 'D5', 'D6', 'D7']},
#                     index=[4, 5, 6, 7])

# df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
#                     'B': ['B8', 'B9', 'B10', 'B11'],
#                     'C': ['C8', 'C9', 'C10', 'C11'],
#                     'D': ['D8', 'D9', 'D10', 'D11']},
#                     index=[8, 9, 10, 11])

# frames = [df1, df2, df3]
# result = pd.concat(frames)
# print(result)

# left = pd.DataFrame({'key': ['dog', 'cat', 'fish', 'bird'],
#                              'A': ['A0', 'A1', 'A2', 'A3'],
#                              'B': ['B0', 'B1', 'B2', 'B3']})

# right = pd.DataFrame({'key': ['bird', 'fish', 'cat', 'dog'],
#                               'C': ['C0', 'C1', 'C2', 'C3'],
#                               'D': ['D0', 'D1', 'D2', 'D3']})

# result = pd.merge(left, right, on='key')

# print(result)

# left = pd.DataFrame({'city': ['Springfield', 'Springfield',
#                                   'Dover', 'Chicago'],
#                          'state': ['IL', 'OH', 'DE', 'IL'],
#                          'A': ['A0', 'A1', 'A2', 'A3'],
#                          'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'city': ['Cleveland', 'Dover',
#                                        'Springfield', 'Chicago'],
#                               'state': ['OH', 'NH', 'IL', 'IL'],
#                                         'C': ['C0', 'C1', 'C2', 'C3'],
#                                         'D': ['D0', 'D1', 'D2', 'D3']})

# result = pd.merge(left, right, on=['city', 'state'])
# print(left, '\n')
# print(right, '\n')
# print(result)




dobs = pd.DataFrame({'name': ['Suzy', 'Wei','Yulia', 'Arvind'],
                   'day': ['12', '19', '2', '23'],
                   'month': ['Dec', 'Nov', 'May', 'Jul']})

addresses = pd.DataFrame({'name': ['Marisol', 'Arvind','Stephan', 'Suzy'],
                     'city': ['San Francisco', 'Denver', 'Austin', 'Seattle'],
                     'state': ['CA', 'CO', 'TX', 'WA']})

print(dobs, '\n')
print(addresses, '\n')

birthday_address = pd.merge(dobs, addresses, how='left')
print(birthday_address)