# ProjEuler1
# If we list all the natural numbers below 10 that are multiples of 3
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find
# the sum of all the multiples of 3 or 5 below 1000.

import doctest

def mult_3_5(n):
    '''
    Integer -> Integer

    Return the sum of all multiples of 3 or 5 below n

    >>> mult_3_5(10)
    23
    '''
    multList = [i for i in range(n) if i % 3 == 0 or i % 5 == 0]
    return sum(multList)

doctest.testmod()

print(mult_3_5(1000))
