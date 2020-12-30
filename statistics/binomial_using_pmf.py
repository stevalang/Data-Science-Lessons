'''
Number of successes k in n trials with fixed probability p
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

def comb(n, k):
    
    perm = 1

    for i in range(n, n-k, -1):
    
        perm *= i
    
    return int(perm / factorial(k))


'''
PMF: Probability Mass Function
- Giving us the probability of a certain specific outcome
- can answer the binomial questions
- 3 params:
    n : number of trials
    k : represents the number of successes
    p : is the probability of success of singel trial (held constant)

What is the probability in 12 coin flips of a fair coin, that you get 7 heads?

'''

print(binomial_pmf(12, 7, 0.5))

'''
Sitting on a park bench you observe geese walking by. There's a probability
of 0.3 that any goose walking by has black feet. What is the probability
that 4 out of the next 12 geese walking by has black feet?
'''

'''
You are at the party and looking for a vegan girlsfriend. There is 
probability of 0.6 that any of the girls on the party will be vegan.
What is the probability that 1 out of 10 girls that you will talk with
on the party will be vegan.
'''