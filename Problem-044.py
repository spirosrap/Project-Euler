import itertools
import math
from math import *
import decimal
from decimal import *
from collections import deque

def pn(n):
	return n*(3*n-1)/2
	
pentagonal=[]	
for i in range(1,2000000):
	pentagonal.append(pn(i))
table=[]
def check(n):
	num=pn(n)
	for i in range(n,0,-1):
		for j in range(n,0,-1):
			if(pn(i)+pn(j)==num):
				table.append((i,j))
				if(abs(pn(i)-pn(j)) in pentagonal):
					print i,j
		if(pn(i)+pn(i-1)<num):
			break
				
for k in range(1,3000):
	for i in range(k,3000):
		athroisma=pn(i)+pn(k)
		afairesi=abs(pn(i)-pn(k))
		r1=(3+math.sqrt((9+24*athroisma)))/6
		r2=(3+math.sqrt((9+24*afairesi)))/6
		if athroisma in pentagonal[int(r1)-1:int(r1)] and afairesi in pentagonal[int(r2)-1:int(r2)]:
			print pn(k),pn(i),athroisma,pn(int(r1))

				
