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

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

D=[]

for i in range(2,1001):
	if is_square(i)==False:
		D.append(i)
		
def periods(S):
	m0=0
	d0=1
	a0=int(S**(1/2.0))
	a00=a0
	a=[]
	s=0
	a.append(a0)
	check=[]	
	while(True):
		m0=d0*a0-m0
		d0=(S-m0**2)/(d0*1.0)
		a0=int((a00+m0)/(d0*1.0))		
		if ((m0,d0,a0)) in check:
			break
		a.append(a0)		
		check.append((m0,d0,a0))
		s+=1
		
	p=[]
	q=[]
	r=len(a)-1-1
	if(r!=0 and r%2==0):
		a=a+a[1:len(a)-1]
	p.append(a[0])#p0
	p.append(a[0]*a[1] + 1)#p1
	q.append(1) #q0
	q.append(a[1]) #q1
	for i in range(2,len(a)):
		p.append(a[i]*p[i-1]+p[i-2])
		q.append(a[i]*q[i-1]+q[i-2])
	if(r%2==0):
		retP=p[2*r+1]
		retQ=q[2*r+1]
	else:
		retP=p[r]
		retQ=q[r]
								
	return a,p,q,retP,retQ
	
print periods(13)
print periods(2)
print periods(3)
print periods(5)
print periods(6)
print periods(7)

xs=[]
max=0
for d in D:
	if(periods(d)[3]>max):
		max=periods(d)[3]
		print d
	

