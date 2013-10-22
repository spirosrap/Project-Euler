
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

def removeFromList(n,l):
	lis=[]
	for iL in range(0,len(l)):
			if(n == l[iL]):
				lis=l[:iL]+l[iL+1:]
	return lis
	
n=0
triangle=[]
square=[]
pentagonal=[]
hexagonal=[]
heptagonal=[]
octagonal=[]
nums=[]
while(n<=10000):		
	t=n*(n+1)/2
	if(t>=1000 and t<=10000):
		triangle.append(t)
	t=n*n
	if(t>=1000 and t<=10000):
		square.append(t)
	t=n*(3*n-1)/2
	if(t>=1000 and t<=10000):
		pentagonal.append(t)
	t=n*(2*n-1)
	if(t>=1000 and t<=10000):
		hexagonal.append(t)	
	t=n*(5*n-3)/2
	if(t>=1000 and t<=10000):
		heptagonal.append(t)
	t=n*(3*n-2)	
	if(t>=1000 and t<=10000):
		octagonal.append(t)
	n+=1
	
nums=[]
nums.append(triangle)
nums.append(square)
nums.append(pentagonal)
nums.append(hexagonal)
nums.append(heptagonal)
nums.append(octagonal)

def check2(n1,n2):
	tempN1=str(n1)
	tempN1=tempN1[2:4]
	tempN2=str(n2)
	tempN2=tempN2[0:2]
	if(tempN2==tempN1):
		return True
	else:
		return False
		
ordered = triangle+square+pentagonal+hexagonal+heptagonal+octagonal			

size=range(0,len(nums))
nums2=[]
for i in size:
	size2=removeFromList(i,size)
	for j in size2:
		for n1 in nums[i]:
			for n2 in nums[j]:
				if(check2(n1,n2)):
					size3=removeFromList(j,size2)
					for i1 in size3:
						size4=removeFromList(i1,size3)
						for j1 in size4:
							for n11 in nums[i1]:
								for n22 in nums[j1]:
									if(check2(n2,n11) and check2(n11,n22)):
										size5 = removeFromList(j1,size4)
										for i2 in size5:
											size6=removeFromList(i2,size5)
											for j2 in size6:
												for n111 in nums[i2]:
													for n222 in nums[j2]:
														if(check2(n22,n111) and check2(n111,n222) and check2(n222,n1)):
															nums2.append(((n1,i),(n2,j),(n11,i1),(n22,j1),(n111,i2),(n222,j2)))
															break
	
	print nums2