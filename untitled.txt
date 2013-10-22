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
	
def check(n1,n2):
	nl1=list(str(n1))	
	nl2=list(str(n2))
	
	for i in range(0,len(nl1)):
		if nl1[i] in nl2:
			None
		else:
			return False
	return True
	
for i in range(1,150000):
	if(check(2*i,3*i) and check(3*i,4*i) and check(4*i,5*i) and check(6*i,5*i)):
		print i		
