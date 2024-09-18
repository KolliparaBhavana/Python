import math
def is_odd(n):
    if n%2!=0:
        return True
    #end-if
    return False
def is_even(n):
    if n%2==0:
        return True
    #end-if
    return False
def is_prime(n):
    n_sqrt=int(math.sqrt(n))
    for i in range(2,n_sqrt+1):
        if(n%i==0):
            return False
        #end-if
    #end-for
    return True