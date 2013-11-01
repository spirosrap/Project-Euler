from math import exp,pi,sqrt,log
from decimal import *
getcontext().prec = 102


def sumOfNums(num):
    string = str(Decimal(num).sqrt())
    pinakas = list(string[0]+string[2:101])
    for i in range(0,len(pinakas)):
        if(len(pinakas)!=1):
            pinakas[i]=int(pinakas[i])
        else:
            pinakas[i]=0        
    return sum(pinakas)

s=0
for i in range(101):
    print sumOfNums(i),i    
    s+=sumOfNums(i)
    
print s    
    