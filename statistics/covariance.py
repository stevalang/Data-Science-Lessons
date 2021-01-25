import numpy as np

gdp_05_19 = [3.5, 2.9, 1.9, -0.1, -2.5, 1.6, 2.2, 1.8, 2.5, 2.9, 1.6, 2.5]

sp500_05_19 = [3, 13.62, 3.54, -38.49, 23.45, 12.78, 0, 13.41, 29.6,11.39, -0.73, 9.54, 19.42, -6.24, 28.8]


def cov_corr(data1, data2, pop=False):

    if pop:
        coeff = 1 / len(data1)
        ddof = 0
    else:
        coeff = 1 / (len(data1) - 1)
        ddof = 1

    data1_arr = np.array(data1)
    data2_arr = np.array(data2)

    cov = coeff * sum((data1_arr - np.mean(data1)) * (data2_arr - np.mean(data2_arr)))
    corr = cov / (np.std(data1_arr,ddof) * np.std(data2_arr, ddof))

    return cov, corr

