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

	
def factorials_dict():
    """Create a dictionary of factorials 0 - 9"""
    d = {}
    for i in xrange(0, 10):
        d[i] = math.factorial(i)
    return d

factorials = factorials_dict()

def facto(n):
	s=0
	st=str(n)
	for i in range(0,len(str(n))):
		s+=factorials[(int(st[i]))]		
	return s	


def cycle(n):
	flag = True
	a=[]
	b=facto(n)
	while(flag):
		try:
			a.index(b)
			flag=False
			break
		except ValueError:
			a.append(b)			
			b=facto(b)
			if(len(a)>60):
				break
	return a		

s=0
for i in range(1,1000001):
	if(len(cycle(i))>58):
		print len(cycle(i))
		s+=1
		
print s
		


