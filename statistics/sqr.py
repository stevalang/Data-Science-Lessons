# Define the polynomial for which we are finding a root
def f(x):
    return x ** 12 - 9.651224


# Define f'(x)
def df(x):
    return 12 * x ** 11


# Leave the code below this line untouched!


def newton_raphson(x_n, f, df):
    return x_n - f(x_n) / df(x_n)


x_n = 1.5
tol = 1e-10
n = 0


while True:
    x_p = newton_raphson(x_n, f, df)
    if abs(x_p - x_n) < tol:
        break
    x_n = x_p
    n += 1


print(f"The square root of 2 is approximately {x_n}\nNumber of iterations: {n}")
from math import sqrt
print(sqrt(9.651224))