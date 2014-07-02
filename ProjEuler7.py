# ProjEuler7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13. What is the 10,001st prime number?

import doctest

def genPrimes():
    '''
    -> Int

    Use a generator to create primes which are memoized
    in a list
    '''
    yield 2
    yield 3
    primes_list = [2, 3]
    last = primes_list[-1]

    while True:
        last += 2
        for p in primes_list:
            if last % p == 0:
                break
        # loop falls through without finding a factor
        else:
            primes_list.append(last)
            yield last

def nth_prime(nth):
    '''
    Int -> Int

    Return the nth prime

    >>> nth_prime(1)
    2

    >>> nth_prime(2)
    3

    >>> nth_prime(10)
    29
    '''
    counter = 0
    for i in genPrimes():
        counter += 1
        if counter == nth:
           return i

doctest.testmod()

nth_prime(10001)
