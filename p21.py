import math

def sumProperDivisors(n):
	sum=1
	for i in range (2,int(math.sqrt(n))+1):
		if(n%i==0):
			if(n/i != i):
				sum+=i+n/i
			else:
				sum+=i
	return sum
		
print sumProperDivisors(220)

sum=0
for i in range(1,10000):
	a=sumProperDivisors(i);
	if (sumProperDivisors(a)==i):
		if(a<i):
			sum+=a+i
print sum