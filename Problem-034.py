import math

def computeSum(n):
	string=str(n)
	sum=0
	for i in range(0,len(string)):
		sum+=math.factorial(int(string[i]))
	return sum

for i in range(3,900000):
	if(i==computeSum(i)):
		print i
