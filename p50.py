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
			
num=[]
bound=10000			
for ai in [13]:	
	for bi in range(ai+1,bound):
		if checkNums(ai,bi):
			a=list(set([ai,bi]))
			a.sort()
			num.append((a[0],a[1]))
num = list(set(num))
num.sort()
			
print num

num1=[]			
for n in num:
	for ci in range(n[1],bound):
		if checkNums(n[0],ci) and checkNums(n[1],ci):
			a=list(set([ai,bi]))
			a.sort()			
			num1.append((n[0],n[1],ci))
num1 = list(set(num1))
num1.sort()

print num1

num2=[]

for n in num1:
	for di in range(n[2],bound):
		if checkNums(n[0],di) and checkNums(n[1],di) and checkNums(n[2],di):
			a=list(set([ai,bi]))
			a.sort()			
			num2.append((n[0],n[1],n[2],di))	
print num2
flag=False
for n in num2:
	for ei in range(n[3],bound):
		if checkNums(n[0],ei) and checkNums(n[1],ei) and checkNums(n[2],ei) and checkNums(n[3],ei):
			print n[0],n[1],n[2],n[3],ei
			num2.append((n[0],n[1],n[2],n[3],ei))
			flag=True
			break
	if flag:
		break

