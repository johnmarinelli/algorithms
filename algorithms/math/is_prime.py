"""
Naive implementation of primality test 
code from: http://en.wikipedia.org/wiki/Primality_test
"""

#simple primality test from wikipedia for n > 5
def is_prime(n):
  #if n is less than or equal to 3, then return whether or not n is >= 2
  if n <= 3:
    return n >= 2

  #check if n is divisible by 2 or 3
  if n % 2 == 0 or n % 3 == 0:
    return False

  #finally, in the range of 5 to sqrt(n)+1 incrementing by 6,
  #check if n is divisible by those primes or the odd numbers between those primes
  #follows the property that prime numbers > 5 = 6k +- 1
  for i in range(5, int(n ** 0.5) + 1, 6):
    if n % i == 0 or n % (i+2) == 0:
      return False

  return True
