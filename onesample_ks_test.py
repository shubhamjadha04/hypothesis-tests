import numpy as np
import math as m


# gaussian cdf 
def Gaussian_CDF(data):
    result=[]
    meu=np.mean(data)
    sd=np.std(data)
    for i in data:
        a1=(i-meu)/(np.sqrt(2)*sd) 
        ans=1/2*(1+m.erf(a1)) 
        result.append(ans) 
    return np.array(result)

# empirical cdf
def Empirical_CDF(data):
    sorted_data=np.sort(data)
    ecdf_values=[] 
    i=0
    while i<len(sorted_data):
        var=(i+1)/len(sorted_data) 
        ecdf_values.append(var)
        i+=1 
    return ecdf_values

# original ks one sample test
def ks_onesample_test(data):
    data = np.sort(data)
    GCDF = Gaussian_CDF(data)
    ECDF = Empirical_CDF(data)

    sup_diff = 0
    i = 0
    while i < len(data):
        diff = abs(ECDF[i] - GCDF[i])
        if diff > sup_diff:
            sup_diff = diff
        i+=1

    n = len(data)
    CV = 1.358/np.sqrt((n+n)/n*n)

    if sup_diff > CV:
        print("H0 is rejected.")
        print("The sample data does not follow the specified theoretical distribution")

    else:
        print("Fail to reject H0")
        print("The sample data follows the specified theoretical distribution")




    
