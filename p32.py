import itertools
import math
import decimal
from decimal import *
from collections import deque
import prime

def containsAll(n):
	num=123456789
	numbers=list(str(num))	
	string=list(n)
	if(len(string)==9):
		for i in range(0,len(numbers)):
			if numbers[i] in string:
				None
			else:
				return False
	else:
		return False
	return True

for i in range(1,1000):
	for j in range(i,1000):
		k=i*j
		string=str(i)+str(j)+str(k)
		if(containsAll(string)):
			print i,j,k			

for i in range(1,5):
	for j in range(1000,10000):
		k=i*j
		string=str(i)+str(j)+str(k)
		if(containsAll(string)):
			print i,j,k			

