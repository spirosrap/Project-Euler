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

def divisors(n):
	print 1
	for i in range (2,int(math.sqrt(n))+1):
		if(n%i==0):
			if(n/i != i):
				print i,n/i
			else:
				print i
	return sum

def category(n):
	if(sumProperDivisors(n)==n):
		return 0 #perfect Number
	elif(sumProperDivisors(n)< n):
		return 1 #deficient
	elif(sumProperDivisors(n)> n):
		return 2 #abundant
	else:
		return -1


abundants=[]		
for i in range (1,20162):
	if category(i)==2:
		abundants.append(i)

aband={}
for i in range(len(abundants)):
	aband[str(abundants[i])]=i

def looping(n):
	for i in range(0,len(abundants)):
		if(abundants[i]>n):
			return i
		else:
			return len(abundants)


def check(n):
	for i in range(0,looping(n)):
		for j in range(0,looping(n)):
			sum=abundants[i]+abundants[j]
			if(sum==n):
				return True;
twos=[]				

def twoAbund():
	for i in range(0,len(abundants)):
		for j in range(i,len(abundants)):
			twos.append(abundants[i]+abundants[j])

twoAbund()
print "done"
current=1
twos.sort()

table=[]
for i in range(0,twos[len(twos)-1]):
	table.append(i+1)
print table

for i in twos:
	table[i-1]=0
print table

print sum(table[0:20161])				
#print twos

#nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]


"""
#4179871



#Every number greater than 20161 can be expressed as a sum of two abundant numbers.
"""