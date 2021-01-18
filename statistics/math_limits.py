import numpy as np

def f(x):
    return x ** 2 if x != 2 else 'Undefined'

# print(f(2))


x = np.array([10 ** (-k) for k in range(1, 9)])
# print(x)

# for val in 2 - x:
#     print(f(val))

for val in 2 + x:
    print(f(val))

