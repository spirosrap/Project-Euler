#!/usr/bin/python
import math
from math import *
import itertools
import decimal
from decimal import *
from collections import deque
from prime import Prime

def expand(n):
	if(n==1):
		return (3,2)
	else:
		p=expand(n-1)
		return (p[0]+2*p[1],p[0]+p[1])
sum=0	

for i in range(1,1000):
	p=expand(i)
	if len(str(p[0]))>len(str(p[1])):
		sum+=1
p=expand(999)		
p1000=(p[0]+2*p[1],p[0]+p[1])
if len(str(p[0]))>len(str(p[1])):
	sum+=1
print sum