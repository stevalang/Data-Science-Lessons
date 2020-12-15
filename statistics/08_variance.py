from mean.py import mean


def variance(lst, sample=True):

    mean_ = mean(lst)
    total = 0

    for num in lst:
        total += ((num - mean_)**2)

    if sample:
        return total/ (len(lst) - 1)
    return total/len(lst)
