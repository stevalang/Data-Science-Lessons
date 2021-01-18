import numpy as np

# Define the function you're integrating

def f(x):
    return 2/3 * (x * ((4*(x**2 )+ 12)**(1/2)))


# Define an integration function

def riemann_sum(f, a, b, n):
    
    '''
    Approximate the area under the curve 'f' from 'a' to 'b' via 
    a Riemann summation of 'n' rectangles using the midpoint rule.

    Parameters
    ----------
        f : function
            The function over which to integrate
        a : float
            The lower bound of the integral
        b : float
            The upper bound of the integral
        n : int
            The number of rectangles to use

    Returns
    -------
        float
            An approximation of the definite integral
            of 'f' over the interval ['a', 'b'].
    '''

    # The width of the rectangles, delta x
    dx = (b - a) / n

    # A length - n vector of x-values starting at a + dx/2 and ending at b - dx/2
    xi = np.linspace(a + 0.5*dx, b - 0.5*dx, n)

    # A length - n vector of just dx ([dx, dx,..])
    dx_vec = np.array([dx]*n)

    # Evaluate f(x) for all xi values
    fxi = f(xi)

    # Return the dot product of f(xi) the vector of [dx, dx, ..]
    # This is just a quick and easy way to take the sum of the products f(x_i)*dx
    return np.dot(fxi, dx_vec)

print(riemann_sum(f, 0, 1, 10))