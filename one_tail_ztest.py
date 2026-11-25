import numpy as np
from scipy.stats import norm

def one_sample_ztest(data, population_mean, population_std,sig_level=0.05):
    n = len(data)

    sample_mean = np.mean(data)

    standard_error = (population_std/np.sqrt(n))

    z_stats = (sample_mean - population_mean) / standard_error

    CV = norm.ppf(1-sig_level/2)

    if z_stats > CV:
        print("H0 is rejected")
        print("there is significant difference in sample mean and population mean")

    else:
        print("Fail to reject H0")
        print("there is no significant difference in sample mean and population mean") 







