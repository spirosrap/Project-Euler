import re

#!/usr/bin/python
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



def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def periods(S):
	def m(n):
		if n==0:
			return 0
		else:
			return d(n-1)*a(n-1)-m(n-1)

	def d(n):
		if n==0:
			return 1
		else:
			return (S-m(n)**2)/d(n-1)

	def a(n):
		if n==0:
			return int(S**(1/2.0))
		else:
			return int((a(0)+m(n))/(d(n)*1.0))
	
	return a(0),a(1),a(2),a(3),a(4),a(5),a(6),a(7),a(8),a(9),a(10),a(11)
	
def periods2(S,n):
	m0=0
	d0=1
	a0=int(S**(1/2.0))
	a00=a0
	p=[]
	p.append(a0)
	for i in range(0,n):
		m0=d0*a0-m0
		d0=(S-m0**2)/(d0*1.0)
		a0=int((a00+m0)/(d0*1.0))
		p.append(a0)
		
	#toString from list
	st=""
	for i in range(0,len(p)):
		st+=str(p[i])
		st+=" "		
	return st
	
	
	
	
p=periods2(2,50)
print p
regex = re.compile(r'(.+? .+?)( \1)+')
match = regex.search(p)
print match.group(1)    # repeating portion

nums=[]
for i in range(2,10000):
	if is_square(i)==False:
		nums.append(i)

print len(nums)
s=0
for i in nums:
	n=10
	p=periods2(i,n)
	regex = re.compile(r'(.+? .+?)( \1)+')
	match = regex.search(p)
	if(match):
		p

print s
