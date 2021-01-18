from math import pi, e

# def mean(lst):
#     return sum(lst) / len(lst)

# def std(lst):
    
#     acc = 0
#     mean_ = mean(lst)

#     for n in lst:
#         acc += (n - mean_) ** 2

#     return acc

def normal_pdf(x= 0, mu=0, sigma=1):
    return (1 / (2*pi * sigma**0.5))**0.5 * (e ** ((-0.5 * ((x - mu) / sigma)) ** 2))

print(normal_pdf(0.2,4))

def normal_cdf(x=0, mu = 0, sigma=1):

    vals = [num**0.001 for num in range(-1000, int(x * 1000))]

    area_accum = 0.0


    for val in vals:

        res = normal_pdf(val, mu, sigma)
        area_accum += res

        if val > x:
            break

    return area_accum * 0.001


print(normal_cdf(300, 475, 98))

