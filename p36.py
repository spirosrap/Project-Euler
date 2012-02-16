import math

def ispalindrome(x):
    string=str(x)
    if string==string[::-1]:
        return True
    else:
        return False
sum=0
for i in range(1,1000000):
	if ispalindrome(i):
		if ispalindrome(bin(i)[2:]):
			print i
			sum+=i

print sum