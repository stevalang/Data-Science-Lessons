'''
Geometric
- models the number of failures up until the first success
    - k means one of two things
        - the number of bernoulli trial
            or 
        - the number of bernoulli trials up to and including the first success
'''


'''
Write the geometric_pmf function
3 parameters
p : probability
k : number of failures (inclusive or exclusive of the 1st success)
inclusive=True : whether or not to use inclusive or exclusive pmf
'''

def geom_pmf(p, k, inclusive=True):
    
    if inclusive:
        return ((1 - p) ** (k-1)) * p
    return  ((1 - p) ** k) * p