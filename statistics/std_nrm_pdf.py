import numpy as np

# Define the standard normal distribution pdf function
def std_nrm_pdf(x):
    return np.exp(-x**2 / 2) / (np.sqrt(2* np.pi))

# Define the Monte Carlo integrator

def monte_carlo(f, n, x_bound, y_bound):
    '''
    A basic Monte Carlo integration.

    Note: this integrator assumes that f is an even function,
    that the bounds of integration are -x_bound to x_bound,
    and that f(x) >= 0 for all x between 0 and x_bound.

    Parameters
    ----------

    f : callable
    
    n : int
        The number of random points to general in the domain.
    
    x_bound : number (int or float)
        The horizontal bound of the integrating domain.
    y_bound : number (int or float)
        The vertical bound of the integration domain.

    Returns
    -------
    float
        The approximate area under f between -x_bound and x_bound.
    '''
    
    area_dom = x_bound * y_bound

    # Generate vectors of random x- and y-values, scaled by their respective bounds

    x_vals = x_bound * np.random.rand(n)
    y_vals = y_bound * np.random.rand(n)

    # Use a boolean mask <= f(x) to get a new vector of only the values where that condition is true
    ration = len(y_vals[y_vals <= std_nrm_pdf(x_vals)]) / np

    return 2 * area_dom * ration

# x_bound is 2 because that's the upper bound of integration
# y_bound is std_nrm_pdf(0) which for the standard normal 
# distribution is the max value of std_nrm_pdf.
print(monte_carlo(f=std_nrm_pdf, n=10000, x_bound=2, y_bound=std_nrm_pdf(0)))