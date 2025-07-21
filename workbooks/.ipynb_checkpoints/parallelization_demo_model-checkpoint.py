# import the necessary math package for the binomial
import math


# fast calculation of binomial
def binomial(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

    
# let's make up a function that takes some time to solve
def log_sum_binomial(n, rand_id):
    
    out_val = math.log(sum(binomial(n, i) for i in range(0, n + 1)))

    # return the output value and a tuple
    return (rand_id, out_val)


# function for synchronous parallelization
def log_sum_binomial_sync(n, rand_id, dict_ret):
    
    out_val = math.log(sum(binomial(n, i) for i in range(0, n + 1)))

    dict_ret.update({rand_id: out_val})
    # return the output value and a tuple
    return (rand_id, out_val)
    