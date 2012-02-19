#!/usr/bin/python
import math
from math import *
import itertools
import decimal
from decimal import *
from collections import deque
from prime import Prime
	
p = Prime()
L = p.factorize(644)

primes=[]
for i in range(2,10000):
	if p.factor(i)==None:
		primes.append(i)

sum=0
i=0
j=0
for j in range(0,60):
	max=600	
	while(max>0):
		i=j
		while(i<max+j):
			sum+=primes[i]
			i+=1
		if(p.factor(sum)==None and sum>900000 and sum<1000000):
			print sum,i-1-j
		max-=1			
		sum=0		
