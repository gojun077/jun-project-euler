# Project Euler Problem 6
# Find the difference between the sum of the squares of the first 
# 100 natural numbers and the square of the sum.

def diffSquare(n):
	sum_sq = 0
	sum1 = 0
	for i in range(1, n + 1):
		sum_sq += i**2
		sum1 += i
	sq_sum = sum1**2
	print(sum_sq)
	print(sq_sum)
	return (sq_sum - sum_sq)

#print(diffSquare(10)) # test case should return 385, 3025, 2640
print(diffSquare(100))

