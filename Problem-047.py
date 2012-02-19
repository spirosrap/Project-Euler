import math
from math import *
import itertools
import decimal
from decimal import *
from collections import deque

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]   # Ensure that this is initialised with at least 1 prime
prime_dict = dict.fromkeys(prime_list, 1)
lastn      = prime_list[-1]

def _isprime(n):
    ''' Raw check to see if n is prime. Assumes that prime_list is already populated '''
    isprime = n >= 2 and 1 or 0
    for prime in prime_list:                    # Check for factors with all primes
        if prime * prime > n: break             # ... up to sqrt(n)
        if not n % prime:
            isprime = 0
            break
    if isprime: prime_dict[n] = 1               # Maintain a dictionary for fast lookup
    return isprime

def _refresh(x):
    ''' Refreshes primes upto x '''
    global lastn
    while lastn <= x:                           # Keep working until we've got up to x
        lastn = lastn + 1                       # Check the next number
        if _isprime(lastn):
            prime_list.append(lastn)            # Maintain a list for sequential access

def factors(n):
    ''' Returns a prime factors of n as a list '''
    _refresh(n)
    x, xp, f = 0, prime_list[0], []
    while xp <= n:
        if not n % xp:
            f.append(xp)
            n = n / xp
        else:
            x = x + 1
            xp = prime_list[x]
    return f


for i in range(100000,150000):
	fac1=len(sorted(set(factors(i))))
	if(fac1==4):
		fac2=len(sorted(set(factors(i-1))))
		if(fac2==4):
			fac3=len(sorted(set(factors(i-2))))
			if(fac3==4):
				fac4=len(sorted(set(factors(i-3))))
				if(fac4==4):
					print i,i-1,i-2,i-3
					print factors(i)
					print factors(i-1)
					print factors(i-2)
					print factors(i-3)		
					break
		
	
