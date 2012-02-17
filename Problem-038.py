import itertools
import math
import decimal
from decimal import *
from collections import deque
import prime

def containsAll(n):
	num=123456789
	numbers=list(str(num))	
	string=list(str(n))
	if(len(string)==9):
		for i in range(0,len(numbers)):
			if numbers[i] in string:
				None
			else:
				return False
	else:
		return False
	return True

for i in range(1,10000):
	string=""
	for n in range(1,10):
		string+=str(n*i)
		if(containsAll(int(string)) and len(string)<10):
			print i,n
			print string
			break