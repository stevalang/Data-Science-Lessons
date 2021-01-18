import scipy.stats as stats

s = 2.75
n = 50

sigma_xbar = s / n**.5

print(stats.t.interval(alpha=0.95, df=n-1, loc=39.9, scale= sigma_xbar))