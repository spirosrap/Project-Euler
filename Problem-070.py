#!/usr/bin/python
import re
import math
from math import *
import itertools
import decimal
from decimal import *
from collections import deque
from prime import Prime
import operator
import string
from sets import Set

def isPerm(n1,n2):
	s1=list(str(n1))
	s2=list(str(n2))	
	s1.sort()
	s2.sort()
	if s1==s2:
		return True
	else:
		return False
		
def divisors(n):
	div=[]
	for i in range (2,int(math.sqrt(n))+1):
		if(n%i==0):
			if(n/i != i):
				div.append(i)
				div.append(n/i)
			else:
				div.append(i)
	return div

p = Prime()	
primes=[]
nfn=[]	
def ffn(n):
	if p.factor(n)==None:
		return (n/((n-1)*1.0),n-1,n,0,[])
	else:
		div=divisors(n)
		f=n
		j=0
		factors=[]
		for d in div:
			if p.factor(d)==None:
				f=f/d
				f*=(d-1)
				factors.append(d)
				j+=1
		return (n/(f*1.0),f,n,j,factors)
		
pa=[]


primes=[]
for i in range(2,4000):
	if p.factor(i)==None:
		primes.append(i)
			
for ip1 in range(0,len(primes)):
	for ip2 in range(ip1,len(primes)):
		a=ffn(primes[ip1]*primes[ip2])
		if(isPerm(a[1],a[2])):
			pa.append(a)		

pa.sort()	
print pa
			
		
"""
check=[]
for p1 in primes:
	n=p
	while(n<10000000):
		n*=p
		f=(n/p)*(p-1)
		print n,f
        check.append((n,f))

		"""