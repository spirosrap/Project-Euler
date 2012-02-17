trunc = []
PRIMES = {}
discounted = [2,3,5,7]

_primes = open('/Users/spirosrap/Dropbox/euler/primes1.txt').readlines()
_primes = [p.strip().replace('    ', ' ').replace('   ', ' ').replace('  ', ' ') for p in _primes]
_primes = [p.split(' ') for p in _primes]
for _p in _primes:
	for p in _p:
		PRIMES[p] = int(p)

print PRIMES["3793"]