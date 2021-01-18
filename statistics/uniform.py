from random import choice

def get_bit():
    return choice([0,1])


def get_binary(n=8):
    return [get_bit() for x in range(n)]

# print(get_binary())

def get_float(n=8):

    bin_list = get_binary(n)
    float_accum = 0.0

    for idx, bit in enumerate(bin_list, 1):
        float_accum += bit * 0.5 ** idx
    
    return float_accum, bin_list

# print(get_float())
from math import e

def exponential_pdf(lmbda,x):
    if x < 0: return 0
    return lmbda * (e ** (-lmbda * x))

def exponential_cdf(lmbda, x):
    if x < 0: return 0
    return 1 - (e ** (-lmbda * x))

def exponential_mean(lmbda):
    return 1 / lmbda

def exponential_variance(lmbda):
    return 1 / (lmbda ** 2 )

def exponential_std(lmbda):
    return exponential_variance(lmbda) ** 0.5
'''
The exponential distribution can be use 
'''

print(1 - exponential_cdf(0.1, 10))
print(exponential_mean(0.1))
print(exponential_variance(0.1))
print(exponential_std(0.1))