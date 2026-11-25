import numpy as np

def permutation_test(data1,data2,no_of_permutation, sig_level):
    meu1 = np.mean(data1)
    meu2 = np.mean(data2)
    #  calculatinng the original diff
    original_diff = abs(meu1 - meu2)

    # combine the data 
    combine_data = np.concatenate((data1, data2))
    

    # calculating expermental diff
    diff = []
    for i in range(no_of_permutation):
        shuff_data = np.random.permutation(combine_data)
        sample1 = shuff_data[:len(data1)]
        sample2 = shuff_data[len(data1):]

        diff.append(abs(np.mean(sample1) - np.mean(sample2)))
    
    diff = np.array(diff)
    diff = np.sort(diff)
    p_val = np.sum(diff>=original_diff) / no_of_permutation
    
    
    if p_val <= sig_level:
        print("H0 is rejected")
        print("there is a significant difference.")

    else:
        print("fail to reject the H0.")
        print("there is no significant difference (not enough evidence)")



# data1 = np.random.randint(100, 200, 50)
# data2 = np.random.randint(100, 200, 50)
# no_of_permutation=1000 
# sig_level=0.05
# permutation_test(data1,data2,no_of_permutation,sig_level)