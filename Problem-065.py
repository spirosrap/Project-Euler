#!/usr/bin/python

def comp(table):
	maximum=len(table)-1
	current=maximum
	a=table
	while(current>=0):
		if current==maximum:
			retValue=(1,a[current])
			current-=1			
		else:
			retValue=(retValue[1],retValue[0] + a[current]*retValue[1])
			current-=1
	return (retValue[1],retValue[0])	
	
		
a=[2]
for i in range(1,100):
	a.append(1)
	a.append(2*i)
	a.append(1)
	
b = a[0:100]
numerator=comp(b)[0]
numerator = str(numerator)

sum=0
for i in range(0,len(numerator)):
	sum+=int(numerator[i])

print sum