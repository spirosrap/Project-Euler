from Euler import prime_sieve,is_prime,factor
import math
from math import exp,pi,sqrt,log
primes = prime_sieve(100)



def f(p):
    a = [0]*100
    for k in range(0,len(a)):
        if(k*p<len(a)):
            a[k*p]=1
    return a
    


def multiply(s1,s2):
	res = [0]*(len(s1)+len(s2)-1)
	for o1,i1 in enumerate(s1):
	    for o2,i2 in enumerate(s2):
	        res[o1+o2] += i1*i2
	return res

print primes	
a = multiply(multiply(multiply(multiply(multiply(multiply(multiply(multiply(multiply(multiply(multiply(multiply(multiply(multiply(multiply(multiply
        (multiply(multiply(multiply(multiply(f(2),f(3)),f(5)),f(7)),f(11)),f(13)),f(17)),f(19)),f(23)),f(29)),f(31)),f(37)),f(41)),f(43)),f(47)),f(53)),f(59)),f(61)),f(67)),f(71)),f(73))[:73]
        
print a        
print a[71]
def sopf(p):
    sum=0
    for i in factor(p):
        sum+=i[0]
    return sum    
        
def k(n):
    if n==1:
        return 0
    partsum=0
    for j in range(1,n):
        partsum+=sopf(j)*k(n-j)
    return (1/float(n))*(sopf(n)+partsum)

#print k(18)
