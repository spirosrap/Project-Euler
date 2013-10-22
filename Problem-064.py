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


def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True



def periods2(S,n):
	m0=0
	d0=1
	a0=int(S**(1/2.0))
	a00=a0
	p=[]
	s=0
	p.append(a0)
	check=[]
	for i in range(0,n):
		m0=d0*a0-m0
		d0=(S-m0**2)/(d0*1.0)
		a0=int((a00+m0)/(d0*1.0))
		p.append(a0)
		if ((m0,d0,a0)) in check:
			None
		else:
			check.append((m0,d0,a0))
			s+=1
	return (p,s)

nums=[]
s=0
for i in range(2,10000):
	if is_square(i)==False:
		nums.append(i)
		test = periods2(i,550)
		if(test[1]%2!=0):
			s+=1
print s