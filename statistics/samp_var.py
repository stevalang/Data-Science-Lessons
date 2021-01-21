import scipy.stats as scs


n = 108879

k = 27213

p = 56330/226977

print(scs.binom.cdf(k, n, p))

scs.norm.cdf(k, loc = n*p, scale = (n*p*(1-p))**.5)