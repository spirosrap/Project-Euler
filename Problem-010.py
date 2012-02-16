import math

def isPrime1(num):
    if type(num) != int: return False
    if num == 2: return True
    if num < 2 or num % 2 == 0: return False
    return not any(num % i == 0 for i in range(3, int(math.sqrt(num))+1, 2))


def isPrime(num):
	for i in range(2,int(math.sqrt(num))+1):
		if(num%i==0):
			return False;
	return True;
	
print  isPrime(110000);

