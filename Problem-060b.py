
#!/usr/bin/python
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

p = Prime()
primes=[]
j=0
for i in range(2,2000):
	if(p.factor(i)==None):
		primes.append(i)
		if i==4159:
			print j
		j+=1	

def removeFromList(n,l):
	lis=[]
	for iL in range(0,len(l)):
			if(n == l[iL]):
				lis=l[:iL]+l[iL+1:]
	return lis	

def checkNums(n1,n2):
	str1=str(n1)
	str2=str(n2)
	if p.factor(n1)==None and p.factor(n2)==None:
		if p.factor(int(str1+str2))==None and p.factor(int(str2+str1))==None:
			return True
		else:
			return False

print p.factor(719)
print p.factor(197)
print p.factor(797)
print p.factor(977)
print p.factor(37277)
print p.factor(973727)
print p.factor(372797)
print p.factor(372719)
print p.factor(193727)

num=[]			
for ai in [3,7,11,13]:	
	for bi in range(3,10000):
		if checkNums(ai,bi):
			a=list(set([ai,bi]))
			a.sort()
			num.append((a[0],a[1]))
num = list(set(num))
num.sort()
			
print num			
num1=[]			
for ci in range(3,10000):
	for n in num:
		if checkNums(n[0],ci) and checkNums(n[1],ci):
			num1.append((n[0],n[1],ci))
num1 = list(set(num1))
num1.sort()
			
print num1
			
num2=[]

for di in range(3,10000):
	for n in num1:
		if checkNums(n[0],di) and checkNums(n[1],di) and checkNums(n[2],di):
			num2.append((n[0],n[1],n[2],di))	
print num2

for ei in range(3,10000):
	for n in num2:
		if checkNums(n[0],ei) and checkNums(n[1],ei) and checkNums(n[2],ei) and checkNums(n[3],ei):
			print n[0],n[1],n[2],n[3],ei
			num2.append((n[0],n[1],n[2],n[3],ei))



b1 = [1,2,3,4,5,9,11,15]
b2 = [4,5,6,7,8]
set(b1).intersection( set(b2))
print list(set(b1).intersection( set(b2)))
						
