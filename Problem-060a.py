
#!/usr/bin/python
import math
from math import *
from prime import Prime
from sets import Set

p = Prime()

def checkNums(n1,n2):
	str1=str(n1)
	str2=str(n2)
	if p.factor(n1)==None and p.factor(n2)==None:
		if p.factor(int(str1+str2))==None and p.factor(int(str2+str1))==None:
			return True
		else:
			return False

bound=10000
c=[]
for i in range(0,10000):
	c.append([])
found=False	
for ai in range(3,10000):	
	for bi in range(ai+1,bound):
		if checkNums(ai,bi):
			c[ai].append(bi)
	temp=list(set(c[ai]))
	temp.sort()
	c[ai]=temp
	for bi1 in range(0,len(c[ai])):
		for bi2 in range(bi1,len(c[ai])):
			ch1=checkNums(c[ai][bi1],c[ai][bi2])
			#print ai,c[ai][bi1],c[ai][bi2]
			if(ch1):
				for bi3 in range(bi2,len(c[ai])):
					ch2 = checkNums(c[ai][bi1],c[ai][bi3])
					ch3 = checkNums(c[ai][bi2],c[ai][bi3])
					if ch1 and ch2 and ch3:
						print ai,c[ai][bi1],c[ai][bi2],c[ai][bi3]
						for bi4 in range(bi3,len(c[ai])):
							ch4 = checkNums(c[ai][bi1],c[ai][bi4])
							ch5 = checkNums(c[ai][bi2],c[ai][bi4])
							ch6 = checkNums(c[ai][bi3],c[ai][bi4])
							if(ch4 and ch5 and ch6):
								print ai,c[ai][bi1],c[ai][bi2],c[ai][bi3],c[ai][bi4]
								found=True
					if found:
						break								
	if found:
		break
							
	