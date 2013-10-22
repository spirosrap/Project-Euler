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

def soras(t):
	mini=t[0]
	l=[]
	m=0
	for i in range(1,len(t)):
		if t[i]<mini:
			mini=t[i]
			m=i
	if m!=0:
		for j in range(0,len(t)):
			l.append(t[(j+m)%(len(t))])
						
	return l


def removeFromList(n,l):
	lis=[]
	for iL in range(0,len(l)):
			if(n == l[iL]):
				lis=l[:iL]+l[iL+1:]
	return lis	
	
tabl=[]
for a1 in range(1,7):
	r2=removeFromList(a1,[1,2,3,4,5,6])
	for a2 in r2:
		r3=removeFromList(a2,r2)
		for a3 in r3:
			sum=a1+a2+a3
			r4=removeFromList(a3,r3)
			for b1  in r4:
				r5=removeFromList(b1,r4)
				for b3 in r5:
					r6=removeFromList(b3,r5)
					if(b1+a3+b3==sum):
						for c1 in r6:
							if(c1+b3+a2==sum):
								t=[(a1,a2,a3),(b1,a3,b3),(c1,b3,a2)]
								t.sort()
								if t in tabl:
									None
								else:
									tabl.append(t)


tabl=[]
for a1 in range(1,11):
	r2=removeFromList(a1,[1,2,3,4,5,6,7,8,9,10])
	for a2 in r2:
		r3=removeFromList(a2,r2)
		for a3 in r3:
			sum=a1+a2+a3
			r4=removeFromList(a3,r3)
			for b1 in r4:
				r5=removeFromList(b1,r4)
				for b3 in r5:
					if(b1+a3+b3==sum):
						r6=removeFromList(b3,r5)
						for c1 in r6:
							r7=removeFromList(c1,r6)
							for c3 in r7:
								if(c1+b3+c3==sum):
									r8=removeFromList(c3,r7)
									for d1 in r8:
										r9=removeFromList(d1,r8)
										for d3 in r9:
											if(d1+c3+d3==sum):
												r10=removeFromList(d3,r9)
												for e1 in r10:
													if(e1+d3+a2==sum):
														t=soras([(a1,a2,a3),(b1,a3,b3),(c1,b3,c3),(d1,c3,d3),(e1,d3,a2)])														
														if t in tabl:
															None
														else:
															tabl.append(t)

print tabl
print len(tabl)
