def combinations(n, k):

    return factorial(n) / (factorial(n - k) * factorial(k))
