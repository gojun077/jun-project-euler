# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest
# prime factor of the number 600851475143?

def genPrimes():
	'''uses a generator to create a sequence of primes'''
	yield 2
	yield 3
	primes_list = [2, 3]
	final = primes_list[-1]

    # tests numbers for primality starting from 5 to 49999
	for i in range(50000):
		final += 2
		for e in primes_list:
			if final % e == 0:
				break
		# loop fell through without finding a factor
		else:
			# add new prime to list
			primes_list.append(final)
			yield final

prime_Factors = []
testNum = 600851475143
for i in genPrimes():
	if testNum % i == 0:
		prime_Factors.append(i)
		print(prime_Factors)

print(prime_Factors[-1]) # print last element from list
