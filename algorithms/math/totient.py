from decimal import Decimal
from prime_factors import prime_factors
"""
Euler's totient function:
Counts the number of positive integers less than or equal to n that are relatively prime to n.  Used in the RSA cryptosystem.

If n is negative, it is turned positive.
"""
def totient(n):
    if n < 0:
        n = n * -1

    elif n is 1:
        return n
	
    tnt = n
    primeFactors = []
    prime_factors(n, primeFactors)
     
    #totient function is the product of (1-pn)(1-p(n-1))...(1-p(1)) times 
    for i in primeFactors:
        pf = Decimal(1 / Decimal(i))
        a = Decimal(1 - pf)
        tnt = Decimal(tnt * a)

    return int(tnt)
