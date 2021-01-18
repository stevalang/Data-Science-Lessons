import random
import matplotlib.pyplot as plt
import numpy as np
import statistics as stats

# Create a normal distribution with mu = 5, sd = 2, n = 1000
pop_norm = np.random.normal(5, 2, 10)

# Plot frequency histogram
plt.hist(pop_norm, bins=20)
# plt.show()


def subsample_mean(data, n = 50):
    '''
    Creates and returns a subsample of a dataset, of a given size.
    
    Parameters
    ----------
    data: list-like
        A list of samples of any numeric type

    n: int
        The size of the desired subsample

    Returns
    -------
    mean_:  float
        The mean of the randomly chosen subsamples
    '''

    sample = []

    while len(sample) < n:
        idx = random.choice(range(len(data)))
        sample.append(data[idx])

    return stats.mean(sample)

means = [subsample_mean(data=pop_norm, n=50) for _ in range(1000)]
plt.hist(means, bins=20)
# plt.show()


# Assume prevoius imports  are still available, create uniform distribution
pop_uni = np.random.uniform(0, 10, 1000)

plt.hist(pop_uni, bins=10)
# plt.show()



means = [subsample_mean(data=pop_uni, n=50) for _ in range(1000)]

plt.hist(means, bins=20)
# plt.show()