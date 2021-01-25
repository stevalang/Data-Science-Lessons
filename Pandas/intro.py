import pandas as pd

prices = pd.Series([1,1,2,3,5],
    index=["apple", 'pear', 'banana', 'mango', 'jackfruit'])

# print(prices)
# print(prices.index)
# print(prices.iloc[1:3], '\n')
# print(prices['pear'])


invenotry = pd.Series([10, 50, 41, 22], 
                        index=['pear', 'banana', 'mango', 'apple'])

# print(invenotry * prices)


nonunique_inventory = pd.Series([10, 50, 41, 22, 50],
                             index=['pear', 'banana', 'mango', 'apple', 'apple'])


# print(nonunique_inventory * prices)

# print(invenotry > 20)

# print(invenotry.loc[invenotry>20])


# print(prices.mean())
# print(prices.std())
# print(prices.median())
# print(prices.describe())

discount_prices = prices.apply(lambda x: .9 * x if x > 3 else x)
# print(discount_prices)

# print(invenotry.iloc[1:3])


# print(prices.loc[ prices < prices.mean()])


df = pd.DataFrame({'a':[1, 2], 'b':[3, 'x'], 'c':[4, None]})
print(df, '\n')
print(df.info())

print(pd.to_numeric(df['b'], errors = 'coerce'))
