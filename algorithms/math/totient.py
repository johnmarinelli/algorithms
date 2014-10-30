from decimal import Decimal
from prime_factors import prime_factors
"""
Euler's totient function:
Counts the number of positive integers less than or equal to n that are relatively prime to n.
"""

def totient(n):
	if n < 2:
		return n

	tnt = n
	primeFactors = []
	prime_factors(n, primeFactors)

    #remove unnecessary values
	if primeFactors.count(1) > 0:
		primeFactors.remove(1)
	
	if primeFactors.count(n) > 0:
		primeFactors.remove(n)

    #remove duplicates
	primeFactors = list(set(primeFactors))
    
    #totient function is the product of (1-pn)(1-p(n-1))...(1-p(1)) times n
	for i in primeFactors:
		pf = Decimal(1 / Decimal(i))
		a = Decimal(1 - pf)
		tnt = Decimal(tnt * a)
        print primeFactors

	return int(tnt)
