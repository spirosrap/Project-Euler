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
for n in range(2,1000001):
	if p.factor(n)==None:
		nfn.append((n/((n-1)*1.0),n))
	else:
		div=divisors(n)
		f=n
		for d in div:
			if p.factor(d)==None:
				f=f/d
				f*=(d-1)
		nfn.append((n/(f*1.0),n))

print max(nfn)

