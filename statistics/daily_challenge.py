'''
A family has two pets. We know all of the pets are either a dog or cat.
If the family doesn't have a preference of one type of animal over the other
(equal probability of each pet being a dog/cat), and we know that the 
family has one at least one cat; what is the probability that both pets are
cats? 
'''

# Event A = two cats
# Event B = at least one cat

# Conditonal prob.  formula: P(A | B) = P(AB) / P(B) = (1/4) / (3/4) = 1/3

# [CC, CD, DC, DD]
# P(AB) = 1/4
# P(B) = 3/4

# 1/3

### Conf. Intervals Challenges 2 & 3
'''
Suppose that random sample 50 bottles of a specific brand
'''
import scipy.stats as stats
import numpy as np

sample_stddev = 2.75 / np.sqrt(50)

print(stats.t.interval(alpha=0.95, df=49, loc=39.9, scale=sample_stddev))