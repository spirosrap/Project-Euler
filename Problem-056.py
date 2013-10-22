#!/usr/bin/python
import math
from math import *
import itertools
import decimal
from decimal import *
from collections import deque
from prime import Prime
sums=[]
for i in range(1,100):
	for j in range(1,100):
		p=i**j
		lis=list(str(p))
		sum=0
		for k in range(len(lis)):
			sum+=int(lis[k])			
		sums.append(sum)
		
print max(sums)		

	
