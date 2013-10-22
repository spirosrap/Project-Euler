#!/usr/bin/python
import math
from math import *
import itertools
import decimal
from decimal import *
from collections import deque
from prime import Prime

def ispalindrome(x):
    string=str(x)
    if string==string[::-1]:
        return True
    else:
        return False

def reverse(n):
	string=str(n)
	l=""
	for i in range(len(string)-1,-1,-1):
		l+=string[i]
	return int(l)	
	
print reverse(120)
lynchel=[]
for i in range(10,10000):
	num=i+reverse(i)
	j=1
	while(ispalindrome(num)==False and j<50):
		num+=reverse(num)
		j+=1
	if j==50:
		lynchel.append(i)
		print i

print len(lynchel)	
