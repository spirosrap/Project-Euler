#!/usr/bin/python
import math
from math import *
import itertools
import decimal
from decimal import *
from collections import deque
from prime import Prime

p = Prime()
num=1
sumtotal=1
diagonals=[]
diagPrimes=[]
for x in range(1,15000):
	for y in range(1,5):
		num=num+2*x
		diagonals.append(num)
		if p.factor(num)==None:
			diagPrimes.append(num)
	if(len(diagPrimes)*(1.0)/(len(diagonals)+1)*(1.0))<0.10:
		print num**0.5
		break
