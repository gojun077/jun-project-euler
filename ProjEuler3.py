# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest
# prime factor of the number 600851475143?

import doctest

def genPrimes(n):
    '''
    Int -> Int

    Use a generator to create primes which are memoized in a list
    of primes up to n
    '''
    yield 2
    yield 3
    primes_list = [2, 3]
    last = primes_list[-1]

    while last < n:
        last += 2
        for p in primes_list:
            if last % p == 0:
                break
        # loop falls through without finding a factor
        else:
            primes_list.append(last)
            yield last


def findPrimeFactors(n):
    '''
    Int -> ListOf Int

    Return list of prime factors of n

    >>> findPrimeFactors(13195)
    [5, 7, 13, 29]
    '''
    prime_factors = [i for i in genPrimes(int(n**0.5)) if n % i == 0]
    return prime_factors

print(findPrimeFactors(600851475143))
doctest.testmod()
