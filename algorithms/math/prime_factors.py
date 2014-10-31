from math import sqrt
from is_prime import is_prime

"""
Naive implementation of prime decomposition
Given a number 'n', returns an ordered array of prime factors of n.
Doesn't give the exponential powers of prime factors.
If n is negative, it will be turned positive.
If div is less than 1, it becomes 1.  Once div is at 3, we increment by 2's, since all primes are odd.

Algorithm:
Check if div > n.  If so, return array and we're done.
If n is not a multiple of div, increment div and call function again
If n is a multiple of div and div is prime, add div to list.  Divide n by div, increment div, and call function again

Note: Since the default recursion depth is 1000, the largest prime number this function can process is 1987.  You'll need to set recursion depth to a higher number if you want to use this function with a PRIME number larger than 1987.  Composite numbers are restricted by recursion depth as well, but at a much higher upper bound.
"""

def prime_factors(n, array=None, div=1):
  #if first pass, set array to a new instance
  if array is None:
    array = []

  #if n is negative, make it positive
  if n < 0:
    n = n * -1

  #make div a positive int
  if div < 1: 
    div = 1

  inc = 1
  #if div is > 2 we can increment by 2's, because no primes are even other than 2
  if div > 2:
    inc = 2
  
  # if we're at the end point. divisors won't be larger than the square root of input
  if div > n:
    # if array length is still one, then it's a prime number
    if len(array) == 0:
      array.append(n)

    return array

  # n is not a multiple of div, so proceed
  elif n % div != 0:
    return prime_factors(n, array, div+inc)

  # if n is a multiple of div, add it
  else:
    n = n / div
    if div not in array and is_prime(div):
      array.append(div)
    return prime_factors(n, array, div+inc)
