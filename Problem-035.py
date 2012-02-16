import itertools
import math
import decimal
from collections import deque

def computeSum(n):
	string=str(n)
	sum=0
	for i in range(0,len(string)):
		sum+=math.factorial(int(string[i]))
	return sum


def isPrime(num):
	for i in range(2,int(math.sqrt(num))+1):
		if(num%i==0):
			return False;h
	return True;

			

def rotations(n):
	tab=[]
	for i in range(len(str(n))):
		d = deque(str(n))
		d.rotate(i)		
		tab.append(int(''.join(list(d))))
	return tab
	
		
#primes sieve of eratosthenes
def primes(n):
	''' Return a boolean list of all primes < n '''
	s = [False]*2 + [True]*(n-2)
	for i in range(2, int(n**0.5) + 1):
		if s[i]:
			s[i*i : n : i] = [False] * (1 + (n - 1)/i - i)
	return s


p=primes(1000000)
table=[]
for i in range(1,1000000):
	if p[i]:
		rotate=rotations(i)
		flag=True
		for j in rotate:
			if p[j]==False:
				flag=False
				break
		if flag==True:
			table.append(i)

print len(table)