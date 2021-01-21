import numpy as np


#The sample mean and variance
mu_hat = np.mean(data)
sigma_sq_hat = np.var(data, ddof=0)
print("Sample Mean: {0:1.3f}".format(mu_hat))
print("Sample Variance: {0:1.3f}".format(sigma_sq_hat))
# Sample Mean: -0.008
# Sample Variance: 0.484


# Method of moment
a, b = mu_hat - np.sqrt(3 * sigma_sq_hat), mu_hat + np.sqrt(3 * sigma_sq_hat)
print("a = {0:2.2f}".format(a))
print("b = {0:2.2f}".format(b))

# a = -1.89
# b = 1.57


