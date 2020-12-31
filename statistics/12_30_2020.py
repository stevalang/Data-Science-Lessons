def factorial(n):
    
    prod = 1
    
    for num in range(2, n+1):
        prod *=num
    
    return prod

def combinations(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))


def binomial_pmf(n, k, p = 0.5):
    return combinations(n, k) * p**k * (1-p)**(n-k)

def binomial_cdf(n, k_high, p = 0.5):
    
    cdf_probs = 0.0

    for k in range(k_high + 1):
        cdf_probs += binomial_pmf(n, k, p)

    return cdf_probs


# print(binomial_pmf(15, 6, 0.7) + binomial_pmf(15, 7, 0.7))





def is_anagrams(lst):

    out = []

    for w1 in lst:
        for w2 in lst[1:]:
            if w1 != w2 and sorted(w1) == sorted(w2) and w1 not in out:
                out.append(w1)

    return out


words = ['dog', 'god', 'cat', 'act', 'tack', 'star', 'rat', 'rats']

['dog', 'god', 'cat', 'act', 'star', 'rats']

# print(is_anagrams(words))


def order(txt):
    
    d = {}
   
    for w in txt.split():
        for ch in w:
            if ch.isdigit():
                d[ch] = w
            
    d = 
    
    return ' '.join(d.values())

text = "is2 Thi1s T4est 3a"

print(order(text))
