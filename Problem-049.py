#!/usr/bin/python
import math
from math import *
import itertools
import decimal
from decimal import *
from collections import deque
from prime import Prime

def tupleToStr(t):
	i=0
	s=""
	while(i<len(t)):
		s+=str(t[i])
		i+=1
	return s
	
p = Prime()
L = p.factorize(644)

print tupleToStr(list(itertools.permutations("1234"))[0])

def isPerm(n1,n2,n3):
	permsN1=list(itertools.permutations(str(n1)))
	size=len(permsN1)
	perms=[]
	for i in range(0,size):
		perms.append(int(tupleToStr(permsN1[i])))
	if(n2 in perms and n3 in perms):
		print n1,n2,n3
		
isPerm(1487,4817,8147)

for i in range(1000,8000):
	if(p.factor(i)==None and p.factor(i+3330)==None and p.factor(i+2*3330)==None):
		if(isPerm(i,i+3330,i+3330*2)):
			print i,i+3330,i+3330			
			
	
	
