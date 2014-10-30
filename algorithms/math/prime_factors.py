from math import sqrt

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
  for i in range(5, int(n ** 0.5) + 1, 6):
    if n % i == 0 or n % (i+2) == 0:
      return False

  return True



def prime_factors(n, array=[], div=1):
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
      array.append(1)
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
