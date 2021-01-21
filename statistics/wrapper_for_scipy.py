import numpy as np
from scipy import optimize as optim
from log_likelihood_normal_two_parameters import minus_log_likelihood_normal_two_parameters


def wrapper_for_scipy(x):
    """[summary]

    Args:
        x ([numpy array]): [so this simple wrapper unpacks a two element        array and passes the values into the log-likelihood. Similarly, the input data is taken in as a global variable.]
    """
    return minus_log_likelihood_normal_two_parameters(x[0], x[1], x)

# the *maximum* log-likelihood is the one closest to zero,
# therefore: we want to *minimize* minus_log_likelihood

fit_parms = optim.minimize(wrapper_for_scipy, (0, 1), method='Nelder-Mead')
mu, sigma_sq = fit_parms.data

print("Log-Lik Optimal Parameters: mu = {0:2.3f}, sigma_sq = {1:2.3f}".format(mu, sigma_sq)) # Log-Lik Optimal Parameters: mu = -0.008, sigma_sq = 0.484