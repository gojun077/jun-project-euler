# ProjEuler7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13. What is the 10,001st prime number?

def genPrimes():
	'''uses a generator to create a sequence of primes'''
	yield 2
	yield 3
	primes_list = [2, 3]

	final = primes_list[-1]

	for n in range(100):
		final += 2
		for e in primes_list:
			if final % e == 0:
				break
		# loop fell through without finding a factor
		else:
			primes_list.append(final)
			yield final

for i in genPrimes():
	print i
