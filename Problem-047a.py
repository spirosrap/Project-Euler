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
print L

for i in range(100000,150000):
	fac1=len(sorted(set(p.factorize(i))))
	if(fac1==4):
		fac2=len(sorted(set((p.factorize(i-1)))))
		if(fac2==4):
			fac3=len(sorted(set((p.factorize(i-2)))))
			if(fac3==4):
				fac4=len(sorted(set((p.factorize(i-3)))))
				if(fac4==4):
					print i,i-1,i-2,i-3
					print p.factorize(i)
					print p.factorize(i-1)
					print p.factorize(i-2)
					print p.factorize(i-3)		
					break
