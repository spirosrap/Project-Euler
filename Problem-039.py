import itertools
import math
import decimal
from decimal import *
from collections import deque
import prime

for p in range(1,1001):
	sum=0
	for a in range(1,p):		
		for b in range(a,p-a):
			c=p-a-b			
			if(a*a+b*b==c*c):
				sum+=1
	if(sum>=4):
		print sum,p