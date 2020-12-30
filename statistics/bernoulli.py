'''
A random variable represents the outcome of an experiment.

Let Y = the result of processing 3 dice rolls of a 4-sided die through this  equation

Y = sum from i=1 to i=3 of: (1/4) ** i * roll[i]

'''

from random import choice

def  get_three_rolls():
    
    rolls = []

    for _ in range(3):
        rolls.append(choice([1,2,3,4]))

    return rolls


def outcome_of_Y():

    res  = 0.0

    rolls = get_three_rolls()

    for idx, roll in enumerate(rolls, 1):
        res += (1/4) ** idx * roll

    return res

# print(outcome_of_Y())
         

def dic_of_Y(num_sample=100000):
    
    d = dict()

    for _ in range(num_sample):
        outcome = outcome_of_Y()
        if outcome not in d:
            d[outcome] = 0
        d[outcome] +=1

    return d

# for k, v in sorted(dic_of_Y().items()):
#     print(f'{k}: {v}')

'''
Bernoulli trial
single event with a binary outcome, with a set probabiity

If you have a bag of red and blue balls, where you have 30 red balls,
and 70 blue. If you reach into the bag thousands of times and averge
the counts of these balls, what percentage  of your draws would 
you expect to be red?

30%
'''
from random import choice, random

def bernoulli(p_success=0.5):
    
    draw = random()

    if draw < p_success:
    
        return True
    
    return False


# print(bernoulli())

trials = 100000

# print([bernoulli() for _ in range(trials)].count(True) / trials)



'''
Binomial Distribution: series of Bernoulli trials, where we keep a fixed
probability p. We're usually trying to find the probability
of a cerain number of successes k

0 or 1
How do you arrange 3 successes across 5 bernoulli trials

P(A) = |A| / |S|

00000
00001
00010
00011
00111 <- this is a member of the set where you have 3 successes
01011 <- this is a member of the set where you have 3 successes
10011


how many ways can you arrange 1 1 in 5-bit binary?
00001
00010
00100
01000
10000
how many ways can you arrange 2 1s in 5 bit binary?
00011
00101
01001
10001
'''



