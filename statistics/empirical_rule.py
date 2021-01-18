import numpy as np
from scipy.stats import norm

# Standard Normal Distribution
mean, sd = 0, 1

# Proportion for 1, 2, 3 sd's from the mean
one_sd = norm.cdf(sd, mean, sd) - norm.cdf(-sd, mean, sd)
two_sd = norm.cdf(2 * sd, mean, sd) - norm.cdf(-2 * sd, mean, sd)
three_sd = norm.cdf(3 * sd, mean, sd) - norm.cdf(-3 * sd, mean, sd)

# Print the proportions
print("Proportion of values within one sd of the mean:", round(one_sd, 4))
print("Proportion of values within two sd of the mean:", round(two_sd, 4))
print("Proportion of values within three sd of the mean:", round(three_sd, 4))


