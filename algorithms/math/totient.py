from decimal import Decimal
from prime_factors import prime_factors as primeFactorization

def totient(n):
	if n < 2:
		return n

	tnt = n
	primeFactors = []
	primeFactorization(n, primeFactors)

	if primeFactors.count(1) > 0:
		primeFactors.remove(1)
	
	if primeFactors.count(n) > 0:
		primeFactors.remove(n)

	primeFactors = list(set(primeFactors))
	
	for i in primeFactors:
		pf = Decimal(1 / Decimal(i))
		a = Decimal(1 - pf)
		tnt = Decimal(tnt * a)

	return int(tnt)
