import numpy as np
from scipy.stats import norm
from itertools import product
from scipy import optimize as optim

data = np.array([ 12.1085187 ,  12.10867427,  11.21137858,  10.01311363,
                  10.79744224,  13.19280269,  12.44086123,  11.88810057,
                  10.70064104,  11.50382741])


unif_data =  np.array([ 12.74150234,   7.48813381,  11.7510409 ,   5.93809414,
                         4.68964288,   3.70627976,   3.46101127,   6.41408594,
                        10.21747766,   8.71674398,   3.60720254,   9.65162582,
                         6.58295132,   7.31954815,   7.49708025,   5.66849976,
                         6.35144344,  12.08445868,   7.80220492,   9.83051264,
                        12.19963228,   3.59743489,  11.4528373 ,   5.77606004,
                        10.68932553,  10.41001181,  12.31509935,  12.31377402,
                         9.99084698,   5.64170829,   4.8600061 ,   3.83064209,
                         5.80984023,  11.87182268,   8.62335338,   5.27884731,
                        12.12025134,   4.35138826,   4.26284551,   6.70120651,
                        12.91554048,  10.58164179,  10.33635382,   9.18362962,
                         7.06904495,  10.03298992,   5.95876344,   6.05199525,
                        10.08473599,   9.1744051 ])


#The sample mean and variance
# mu_hat = np.mean(data)
# print(type(mu_hat))
# sigma_sq_hat = np.var(data, ddof=0)
# print(sigma_sq_hat)
# print(f"Sample Mean: {mu_hat:.3f}")
# print(f"Sample Variance: {sigma_sq_hat:.3f}")

# Method of moment
# a, b = mu_hat - np.sqrt(3 * sigma_sq_hat), mu_hat + np.sqrt(3 * sigma_sq_hat)
# print(f"a = {a:.2f}")
# print(f"b = {b:.2f}")



def log_likehood_normal_two_parameters(mu, sigma_sq, data):
    """
    Consume the parameters

    Args:
        mu ([type]): [mean]
        sigma_sq ([type]): [variance]
        data_in ([type]): [likelihood of a fixed dataset]
    """
    normal = norm(mu, np.sqrt(sigma_sq))
    likelihoods = [normal.pdf(datum) for datum in data]
    return np.sum(np.log(likelihoods))

def minus_log_likelihood_normal_two_parameters(mu, sigma, data):
    return -log_likehood_normal_two_parameters(mu, sigma, data)


def wrapper_for_scipy(x):
    """[summary]

    Args:
        x ([numpy array]): [so this simple wrapper unpacks a two element        array and passes the values into the log-likelihood. Similarly, the input data is taken in as a global variable.]
    """
    return minus_log_likelihood_normal_two_parameters(x[0], x[1], data)

for mu, sigma_sq in product([-1, 0, 1], [0.5, 1, 2]):
    print("Log-Lik of Two Parameter Normal Model With mu = {0}, sigma_sq={1}: {2:3.2f}".format(mu, sigma_sq, log_likehood_normal_two_parameters(mu, sigma_sq, unif_data)))



# the *maximum* log-likelihood is the one closest to zero,
# therefore: we want to *minimize* minus_log_likelihood

fit_parms = optim.minimize(wrapper_for_scipy, (0, 1), method='Nelder-Mead')

mu, sigma_sq = fit_parms.

# print("Log-Lik Optimal Parameters: mu = {0:2.3f}, sigma_sq = {1:2.3f}".format(mu, sigma_sq)) # Log-Lik Optimal Parameters: mu = -0.008, sigma_sq = 0.484