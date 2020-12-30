'''

CDF is Cumulative Distribution Function
- cumulative implies accumulator
- cumulative provavility between 0 and some value of k (inclusive)

'''
def factorial(n):

    prod = 1

    for num in range(2, n+1):
        prod *= num

    return prod


def combinations(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))

def binomial_pmf(n, k, p):
    return combinations(n, k) * (p ** k) * ((1-p) ** (n-k))

def binomial_cdf(n, k_high, p):


    acc  = 0.0

    for k in range(0, k_high + 1):
        acc += binomial_pmf(n, k, p)

    return acc


'''
You have 14 components in a circuit. At any given time, there is 95%
chance that a given component is functioning. What is the prob. that 12 
or more components are func. in a citcuit that has 20 components?
'''
n = 20
k_high = 11
p = 0.95
# print(1 - binomial_cdf(n, k_high, p))


'''
Suppose you are building some sort of machine that relies on a specific
component. The component is very delicate and the probability of it
failing is 0.32. You decide to install 3 of these components in parallel,
such that they are independent to each other, to ensure that you only
need 1 to work to get your machine working.

What is the probability that 1 or more of these components work?

How many of these components would you need to install in parallel to 
ensure that there is over 99.5% probability that your machine is working
upon any given observation?

'''

def binomial_pmf_dict(n, k_low, k_high, p=0.5):

    d = dict()

    for k in range(k_low, k_high + 1):
        d[k] = binomial_pmf(n, k, p)
    
    return d

d = binomial_pmf_dict(8, 0, 8, p=0.25)

# for k, v in d.items():
#     print(f'{k}: {v}')


def binomial_cdf_dict(n, k_low, k_high, p=0.5):

    d = dict()

    for k in range(k_low, k_high + 1):
        d[k] = binomial_cdf(n, k, p)
    
    return d

d = binomial_cdf_dict(8, 0, 8, p=0.25)

# for k, v in d.items():
#     print(f'{k}: {v}')


from random import choice, random


'''
using choice we are limited to a fixed value of p
'''

def get_bit():
    return choice([0,1])

def generate_n_bits(n=8):
    return [get_bit() for _ in range(n)]
    # lst = []
    # for _ in range(n):
    #     lst.append(get_bit())
    # return lst

# print(generate_n_bits(16))


'''
Write a function called binary_sampling_dict that has two params
    num_bits
    num_samples

return a dict where the keys represent the number of successes,
and the values associated with those keys represent the count of that
number of successes occurring.

{
    0: 35,
    1: 63,
    .....
    num_bits: count of num_bits successes
}
'''


def binary_sampling_dict(num_bits=8, num_samples=1000):

    d = {}

    for _ in range(num_samples):
        k = sum(generate_n_bits(num_bits))
        if k not in d:
            d[k] = 0
        d[k] += 1

    return d

d = binary_sampling_dict()

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')

''' 500 trials of 1000 samples '''

def binary_sampling_clt(n_bits=16, num_samples=1000, num_samples_trials=500):
    
    d_out = dict()

    for _ in range(num_samples_trials):
        d = binary_sampling_dict(n_bits, num_samples)

        for k, v in d.items():

            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)    

    return d_out

d = binary_sampling_clt(16, 1000, 500)

for k, v in sorted(d.items()):
    print(f'{k}: {v / sum(d.values())}') # averaged (observed) probability

    