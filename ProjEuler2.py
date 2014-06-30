# ProjEuler2
# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms will
# be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.

def genFib(n):
    '''
    Int -> Int

    Use generator to calculate terms from fibonacci sequence
    '''
    fibn_1 = 1 # fib(n - 1)
    fibn_2 = 0 # fib(n - 2)
    while fibn_1 < n:
        # fib(n) = fib(n - 1) + fib(n - 2)
        next = fibn_1 + fibn_2
        yield next
        # store previous values in fib sequence
        fibn_2 = fibn_1
        fibn_1 = next

fibList =[i for i in genFib(4000000) if i % 2 == 0]

print(sum(fibList))
