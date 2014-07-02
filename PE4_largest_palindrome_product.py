# ProjEuler4

#A palindromic number reads the same both ways. The largest palindrome
#made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import doctest

def isPalindrome(strNum):
    '''
    Str -> Boolean

    Given an integer in string format, if the original string and its
    chars in reverse order are identical, return True

    >>> isPalindrome('1234')
    False

    >>> isPalindrome('1111')
    True

    >>> isPalindrome('9009')
    True
    '''
    return strNum == strNum[::-1]

def biggest3PalProd():
    '''
    -> List of Int

    Return the largest palindrome that is the product of two 3-digit
    numbers
    '''
    palindrome_list = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if isPalindrome(str(i*j)):
                palindrome_list.append(i*j)

    return max(palindrome_list)

doctest.testmod()

print(biggest3PalProd())
