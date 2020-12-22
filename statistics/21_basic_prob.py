from random import choice

def coin_flip():
    
    flip = ['H', 'T']

    return choice(flip)


def series_of_flips(n):
    
    return [coin_flip() for _ in range(n)]



# print(series_of_flips(5))



def four_flip_samp_space():
    
    flips = ['H', 'T']
    out = []
    
    for i in flips:
        for j in flips:
            for k in flips:
                for l in flips:
                    out.append([i, j, k, l])
    
    return out

outcomes = four_flip_samp_space()

coun_triple_heads = 0
coin_flips = len(outcomes)

for outcome in outcomes:
    if outcome.count('H') == 3:
        coun_triple_heads += 1
print(coun_triple_heads)
print(coun_triple_heads/coin_flips)


'''
Suppose you call the function series_of_flips(14).
What is the probability that you get all 'H' values?

first consider the probability P(H) for one flip:
0.5
'''





