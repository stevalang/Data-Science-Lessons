import pandas as pd

prices = pd.Series([1,1,2,3,5],
              index=['apple', 'pear', 'banana', 'mango', 'jackfruit'])

inventory = pd.Series([10, 50, 41, 22],
              index=['pear', 'banana', 'mango', 'apple'])

discount_prices = prices.apply(lambda x: .9 * x if x > 3 else x)

produce = pd.DataFrame({'price': prices, 
                        'inventory': inventory,
                        'discount_price': discount_prices})


one_select = produce.loc[['pear', 'jackfruit']]

produce['clearance_price'] = produce['price'] * 0.5

two_clearance = produce.iloc[3]

print(two_clearance)
# one_ind = inventory.iloc[1:4:2]
# two_less = inventory.loc[prices < prices.mean()]
# three_onhand = prices['mango'] * inventory['mango']
# three_onhand = (prices * inventory).loc['mango']

# print(one_ind)
# print(two_less)
# print(three_onhand)




# print(produce)

# print(produce.loc['pear':, 'price'])
# print(produce.iloc[2:, 1])
# print(produce.iloc[[0, 2, 3], :])
# print(produce.loc['pear':, 'price'])
# print(produce['discount_price'])
# print(produce.discount_price)

# print(produce.loc[:, produce.max() > 5])


# print(produce.loc[produce['price'] == 1, :])


# produce['inventory_value'] = produce['inventory'] * produce['price']

# print(produce)

# print(produce.drop('inventory_value', axis = 1))

# print(produce)

# produce.drop('inventory_value', axis = 1, inplace=True)

# print(produce)


# a = produce[produce.price >=3]['price'] = 2.50
# print(produce)