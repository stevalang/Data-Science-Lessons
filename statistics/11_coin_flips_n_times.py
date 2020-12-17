from coin_flip.py import coin_flip

def coin_flips_n_times(n):

    acc = []

    for _ in range(n):
        acc.append(coin_flip())

    return acc
