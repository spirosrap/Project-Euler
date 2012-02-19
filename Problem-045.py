import itertools
import math
from math import *
import decimal
from decimal import *
from collections import deque

def pn(n):
	return n*(3*n-1)/2
	

def isPent(m):
	k = (1 + (1+24*m)**.5)/6
	if k == int(k):
		return True
	return False

def isHex(m):
	k = (1 + (1+8*m)**.5)/4
	if k == int(k):
		return True
	return False
	
def isTri(m):
	k = (-1 + (1+8*m)**.5)/2
	if k == int(k):
		return True
	return False
	
for n in range(286,100000):
	t=n*(n+1)/2
	if(isHex(t) and isPent(t)):
		print t

				
