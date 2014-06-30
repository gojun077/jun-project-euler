# Project Euler Problem 6
# Find the difference between the sum of the squares of the first
# 100 natural numbers and the square of the sum.

import doctest

def diffSquare(n):
    '''
    Int -> Int

    Return difference between the sum of the squares of the first n
    natural numbers and the square of the sum of the first n natural
    numbers

    >>> diffSquare(10)
    2640
    '''
    sum_sq = 0
    sum1 = 0
    for i in range(1, n + 1):
        sum_sq += i**2
        sum1 += i
        sq_sum = sum1**2
    return (sq_sum - sum_sq)

doctest.testmod()

print(diffSquare(100))
