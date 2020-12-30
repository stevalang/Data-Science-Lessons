'''
You have a satellite that takes stellar images of random places in space.
On average, each image has 30 stars in it. 
What is the probability that a given image has 25 stars in it
'''

'''
    lmbda represents the average number of successes in a given volume of time
    or space, etc k is the number of successes for which you're trying to
    find the probability
'''
from math import e, factorial

def poisson_pmf(lmbda, k):
    
    return ((lmbda ** k) * (e **(-lmbda))) / factorial(k)

# print(poisson_pmf(30, 25))


'''
e is a constant, a factor of entropy, and it applies in a Poisson process

Criteria or Constraints for Poisson
- an average for a given volume/area/length of time
- each event needs to be independent
- assumption that the rate is consistent (iid. independent and identical
distribution)
'''

'''
Poisson-like phenomena


Phenomenon:
Given an area of grass, it is likely that the distribution of pill bugs
follows a poisson process.

Question:
PMF: in a square foor of your front yard, on avg there are 20 roly
polys in residence. What is the proba that in a given square foot of
your front yard, you find 15 roly pols?
'''

lmbda = 20
k = 15

# print(poisson_pmf(lmbda, k))



'''
Phenomenon:
Cars passing by an intersection at a certain time of day/year, 
for the duration of a fixed amount of time, will likely
follow a Poisson distribution
Question:
PMF: A given intersection will have, on avg, 15 cars pass
through in 10 mintues. What is the probability that 20 cars pass
through in 15 minutes?
'''
lmbda = 15 * (15/10) # this can be a fraction
k = 20

# print(poisson_pmf(lmbda, k))

'''
CDF: Given the same intersection, what is the probability that
more than 15 cars will pass through in 15 minutes?
'''
def poisson_cdf(lmbda, k_high):

    cdf = 0.0

    for k in range(k_high + 1):
        cdf += poisson_pmf(lmbda, k)

    return cdf

lmbda = 15 * (15/10)
k = 15

# print(1 - poisson_cdf(lmbda, k))

'''
Apply a dict to analyze the poisson pmf

keys will be values of k
value will be the probabilities associated with k outcomes

'''

def poisson_pmf_dict(lmbda, low_k, high_k):

    return {k: poisson_pmf(lmbda, k) for k in range(low_k, high_k + 1)}

d = poisson_pmf_dict(10, 0, 30)


# for k, v in d.items():
#     print(f'{k}: {round(v,7)}')


'''
You are observing a phenomenon that follows perfectly a poisson process.
Given a certain number
'''

def poisson_count_exp(lmbda, low_k, high_k, num_samples=10000):
    d = dict()

    for k in range(low_k, high_k + 1):
        
        d[k] = round(poisson_pmf(lmbda, k) * num_samples, 2)

    return d

d = poisson_count_exp(10, 0, 30)

for k, v in d.items():
    print(f'{k}: {v}')


'''
There's a busy intersection in Denver, on average where 30 cars pass by
every 10 minutes. What is the probability that 40 cars will pass by if
observing a new ten minute time period?
'''

lmbda = 30
k = 40

'''
Y
'''