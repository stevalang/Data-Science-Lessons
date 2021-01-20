import pandas as pd
import numpy as np

customers = pd.DataFrame([
    [100, 'Prometheus Barwis', 'prometheus.barwis@me.com', '(533) 072-2779'],
    [101, 'Alain Hennesey', 'alain.hennesey@facebook.com', '(942) 208-8460'],
    [102, 'Chao Peachy', 'chao.peachy@me.com', '(510) 121-0098'],
    [103, 'Somtochukwu Mouritsen', 'somtochukwu.mouritsen@me.com','(669) 504-8080'],
    [104, 'Elisabeth Berry', 'elisabeth.berry@facebook.com','(802) 973-8267']],
    columns = ['customer_id', 'name', 'email', 'phone'])

orders = pd.DataFrame([[1000, 100, 144.82], [1001, 100, 140.93],
                       [1002, 102, 104.26], [1003, 100, 194.60],
                       [1004, 100, 307.72], [1005, 101,  36.69],
                       [1006, 104, 039.59], [1007, 104, 430.94],
                       [1008, 103, 031.40], [1009, 104, 180.69],
                       [1010, 102, 383.35], [1011, 101, 256.20],
                       [1012, 103, 930.56], [1013, 100, 423.77],
                       [1014, 101, 309.53], [1015, 102, 299.19]],
               columns = ['order_id', 'customer_id', 'order_total'])

total_orders = orders.groupby('customer_id')['order_total'].aggregate(np.sum)

customer_total = pd.merge(customers, total_orders, on='customer_id')

customer_total.rename(columns={'order_total': 'total_spend'}, inplace=True)

customer_spend = customer_total[['customer_id', 'name', 'total_spend']]

print(customer_spend)
