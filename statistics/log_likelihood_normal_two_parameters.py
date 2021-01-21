from scipy.stats import norm
import numpy as np

def log_likehood_normal_two_parameters(mu, sigma_sq, data_in):
    """
    Consume the parameters

    Args:
        mu ([type]): [mean]
        sigma_sq ([type]): [variance]
        data_in ([type]): [likelihood of a fixed dataset]
    """
    normal = norm(mu, np.sqrt(sigma_sq))
    likelihoods = [normal.pdf(datum) for datum in data_in]
    return np.sum(np.log(likelihoods))

def minus_log_likelihood_normal_two_parameters(mu, sigma, data_in):
    return -log_likehood_normal_two_parameters(mu, sigma, data_in)

from itertools import product


for mu, sigma_sq in data([-1, 0, 1], [0.5, 1, 2]):
    print("Log-Lik of Two Parameter Normal Model With mu = {0}, sigma_sq={1}: {2:3.2f}".format(mu, sigma_sq, log_likehood_normal_two_parameters(mu, sigma_sq, data)))