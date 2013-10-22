#!/usr/bin/python
import math
from math import *
from prime import Prime
from sets import Set

p = Prime()

def checkTables(l1,l2):
	re=[]
	re=list(set(l1).intersection(l2))
	re.sort()
	return re		

def checkNums(n1,n2):
	str1=str(n1)
	str2=str(n2)
	if p.factor(n1)==None and p.factor(n2)==None:
		if p.factor(int(str1+str2))==None and p.factor(int(str2+str1))==None:
			return True
		else:
			return False

bound=10000
firstDowBound=3
firstUpBound=25
c=[]
for i in range(0,bound):
	c.append([])
found=False	
for ai in range(firstDowBound,firstUpBound):	
	for bi in range(ai+1,bound):
		if checkNums(ai,bi):
			c[ai].append(bi)

#13 5197 5701 6733 8389
for firstNum in range(3,14):
	tabl = c[firstNum]
	if(len(tabl)>4):
		cc=[]
		d=[]
		e=[]
		for bi in range(0,len(tabl)):
			for bj in range(bi+1,len(tabl)):
				if(checkNums(tabl[bi],tabl[bj])):
					cc.append(tabl[bj])
			common=checkTables(tabl,cc)
			#print common,"common"
			cc=[]
			if(len(common)>2):
				#print firstNum,tabl[bi],common,"common1"		
				for ci in range(0,len(common)):
					for cj in range(ci+1,len(common)):
						if(checkNums(common[ci],common[cj])):
							d.append(common[cj])
					common2=checkTables(common,d)
					d=[]
					if(len(common2)>1):
						#print firstNum,tabl[bi],common[ci],common2,"common2"
						for di in range(0,len(common2)):
							for dj in range(di+1,len(common2)):
								if(checkNums(common2[di],common2[dj])):
									e.append(common2[dj])
							common3=checkTables(common2,e)
							if(len(common3)>0):
								None
								print firstNum,tabl[bi],common[ci],common2[di],common3,"common3"		
							e=[]