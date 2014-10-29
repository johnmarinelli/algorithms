import sieve_eratosthenes as sieve

def prime_factors(n, array=[], div=2, inc=0, primes_list=[]):
  # check if we have a list of primes already.  this will be called at the first step
  # jk this algorithm is slow as shit
#  if not primes_list:
#    primes_list = sieve.eratosthenes(n)

  if div < 2: 
    div = 2

#  div = primes_list[inc]
  print(n)
  
  # if we're at the end point
  if div >= n:
    return array

  # n is not a multiple of div, so proceed
  elif n % div != 0:
    return prime_factors(n, array, div+1, inc+1, primes_list)

  # if n is a multiple of div, and it's not in the primes list, add it
  else:
    n = n / div
    if div not in array:
      array.append(div)
    return prime_factors(n, array, div+1, inc+1, primes_list)
