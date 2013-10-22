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

phi=[0,0]
L=1000001
for i in range(2,L):
	phi.append(i)
	
#compute phi
for n in range(2,L):
	if(phi[n]==n):
		for k in range(n,L,n):
			phi[k]*=(n-1.)/n
print phi
print int(sum(phi))

