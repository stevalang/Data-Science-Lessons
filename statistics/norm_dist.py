from math import e, pi,sqrt
# mu = 63
# d = 12

# res = 1 / ((2 * ( d ** 2 )  * pi) * ( e ** ( ( (x - mu) ** 2 ) / (2 * d ** 2) ) ))
# print(res)


# z = (36 - 63) / 12
# print(z)

from scipy.stats import norm
s = 10 / sqrt(18)
print(s)

print(norm.cdf(x=68, loc = 72, scale=s))