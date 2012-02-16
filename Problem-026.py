import itertools
import math
import decimal
from decimal import *
from collections import deque

getcontext().prec = 12000

string=str(Decimal(1)/Decimal(593))
print string
string=str(Decimal(1)/Decimal(577))
print string

values=[]
for i in range(1,1001):
	values.append(0)

k=6
for check in range(1,1000):
	string=str(Decimal(1)/Decimal(check))
	length=len(string)
	i=8
	while(i<1000):
		if(string[length-i:length-2] == string[length+2*(-i+1):length-i]):
			print string[length-i:length-2]
			print string[length+2-2*i:length-i]
			values[check]=i-2
			break
		i+=1

maks=0	
for i in range(0,len(values)):
	if maks>=values[i]:
		None
	else:
		maks=values[i]
		print i
		print maks
