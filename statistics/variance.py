from mean.py import mean


def variance(lst, sample=True):


    out = []
    for num in lst:
        out.append((num - mean(lst))**2)

    if sample:
        return sum(out) / (len(lst) - 1)
    return sum(out)/len(lst)
