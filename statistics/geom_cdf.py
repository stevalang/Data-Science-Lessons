def geom_pmf(p, k, inclusive=True):
    
    if inclusive:
        return ((1 - p) ** (k-1)) * p
    return ((1 - p) ** k) * p

print(geom_pmf(0.005, ))
def geom_cdf_accum(p, k_high, inclusive=True):

    proba = 0.0

    if inclusive:
        starting_at = 1
    else:
        starting_at = 0

    for k in range(starting_at, k_high + 1):
        proba += geom_pmf(p, k, inclusive)
    
    return proba

p = 0.1
k_inclusive = 15
k_exclusive = 14
# print(geom_cdf_accum(p, k_inclusive, inclusive=True))
# print(geom_cdf_accum(p, k_exclusive, inclusive=False))

'''
You are flipping a fair coin. What is the probability that you get your first heads before or on the
7th flip?
'''
p = 0.5
k_inclusive = 7
k_exclusive = 6
# print(geom_cdf_accum(p, k_inclusive, inclusive=True))
# print(geom_cdf_accum(p, k_exclusive, inclusive=False))

p = 0.01
k_inclusive = 14
k_exclusive = 13
# print(geom_cdf_accum(p, k_inclusive, inclusive=True))
# print(geom_cdf_accum(p, k_exclusive, inclusive=False))


def geom_cdf_closed(p, k, inclusive=True):
    
    if inclusive:
        return 1 - (1 - p) ** k 
    return 1 - (1 - p) ** (k + 1)

'''
You have a series of routers transmitting packets of data.
There is a 0.99 probability that a given packet of data
passes through the router.
What is the probability that a given packet of data will pass
successfully through 14 routers?
0.99**14
What is the probability that a given packet will be dropped before
the 15th router it passes through... in other words, on or 
before the 14th router.
'''
p = 0.01
k_inclusive = 14
k_exclusive = 13
# print(geom_cdf_accum(p, 14, inclusive=True))
# print(geom_cdf_accum(p, 13, inclusive=False))
# print(geom_cdf_closed(p, 14, inclusive=True))
# print(geom_cdf_closed(p, 13, inclusive=False))

'''
Geom PMF dict
'''

def geometric_pmf_dict(p, k_high, inclusive=True):
    
    d = dict()

    if inclusive:
        starting_at = 1
    else:
        starting_at = 0
    
    for k in range(starting_at, k_high + 1):
        d[k] = geom_pmf(p, k, inclusive)
    
    return d


d_incl = geometric_pmf_dict(p=0.5, k_high=10, inclusive=True)
d_excl = geometric_pmf_dict(p=0.5, k_high=10, inclusive=False)

# for k, v in d.items():
#     print(f'{k}: {v}')


def geom_cdf_dict(p, k_high, inclusive=True):
    
    d = dict()

    for k in range(inclusive, k_high + 1):
        d[k] = geom_cdf_closed(p, k, inclusive)
    
    return d

d_incl = geom_cdf_dict(p=0.5, k_high=10, inclusive=True)
d_excl = geom_cdf_dict(p=0.5, k_high=10, inclusive=False)

# for k, v in d_incl.items():
#     print(f'{k}:{v}')
# for k, v in d_excl.items():
#     print(f'{k}:{v}')


p = 0.005
k_inclusive = 10
k_exclusive = 9
print(geom_cdf_accum(p, 9, inclusive=True))