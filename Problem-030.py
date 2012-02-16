import math

def computeSum(n):
	string=str(n)
	sum=0
	for i in range(0,len(string)):
		sum+=int(string[i])**5
	return sum

for i in range(2,2000000):
	if(i==computeSum(i)):
		print i
		
print sum([4150,4151,54748,92727,93084,194979])
