import numpy as np
from numpy.random import RandomState


# Monte Carlo integrator
def monte_carlo(f, x_bounds, y_bounds, n=1000000):
    rng = RandomState(123456)
    urng = rng.uniform

    x_min, x_max = min(x_bounds), max(x_bounds)
    y_min, y_max = min(y_bounds), max(y_bounds)
    area_dom = (x_max - x_min) * (y_max - y_min)

    y = urng(y_min, y_max, n)
    points_under_f = y[y <= f(urng(x_min, x_max, n))]

    return area_dom * len(points_under_f) / n


# Leave the code above untouched! Your solutions go below:


# Exponential distribution pdf, with lambda hard-coded
def exponential_pdf(x):
    lam = (7/10) * 2
    return lam * np.exp(-lam * x)


# Define your integrating domain (the rectangle inside of which MC generates points)
x_bounds = (0, 2)
y_bounds = (0, exponential_pdf(0))


# Call monte_carlo() with the proper arguments, leave 'n' with the default v
approx_area = 1 - monte_carlo(exponential_pdf, x_bounds, y_bounds, n=1000000)

print(approx_area)