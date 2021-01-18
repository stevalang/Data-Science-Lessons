from scipy.stats import t
import numpy as np

# Calculate the t-statistic
t_stat = (68 - 72)  / (10 / np.sqrt(18))

#0.019521670182136793

print(t.cdf(x=t_stat, df=18-1))