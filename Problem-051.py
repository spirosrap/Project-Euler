import string
from Euler import prime_sieve, is_prime

 
def eight_prime_family(prime, rd):
  c=0
  for digit in '0123456789':
    n = int(string.replace(prime, rd, digit))
    if (n>100000 and is_prime(n)):
      c=c+1
  return c==8
  
primes = prime_sieve(999999)

for i in xrange(len(primes)):
	for digit in '0123456789':
		if(str(primes[i]).count(str(digit))==3):
			if (eight_prime_family(str(primes[i]), digit)):
				print primes[i]
				exit()
