from math import exp,pi,sqrt,log
from operator import itemgetter
from Euler import gcd
def triangles(L):
    for a in range(1,L/2):
        for b in range(a,L/2):
            s=int((L*L-2*a*b)/2*L)
            for c in range(1,s):
                if a*a+b*b==c*c and a+b+c==L:
                    print a,b,c
                    
#print triangles(12)

def triangles2(L):
    t=[]
    for a in range(1,L/2):
        p=a
        c=int((1/float(2))*(L-p+p*p/(L-p)))
        b=L-p-int(c)
        if a<=b and a*a+b*b==c*c and a+b+c==L:
            t.append((a,b,c,L/float(a)))
    if(len(t)>1):
        print t,L
"""
for i in range(12,120):
    triangles2(i)
"""


asa=[]
for i in range(1500001):
	asa.append(0)

t=[]
#620x620    
#var result = myList.OrderBy(k => k.Item2);
limit=sqrt(1500000/float(2))
print int(limit)+1
for n in range(1,int(limit)+1):
    for m in range(1,int(limit)+1):
        if m>n and gcd(m,n)==1 and (m-n)%2!=0:
            #print m*m-n*n,2*m*n,m*m+n*n,2*m*m+2*m*n
            a=m*m-n*n
            b=2*m*n
            c=m*m+n*n
            L=2*m*m+2*m*n
            t.append((a,b,c,L))
            for s in range(L,1500001,L):
                asa[s]+=1
                
print t

"""
for i in range(0,len(t)):
    for k in range(2,(t[len(t)-1][3]/t[i][3])+1):
        t.append((t[i][0]*k,t[i][1]*k,t[i][2]*k,t[i][3]*k))


lastl=t[len(t)-1][3]
length=len(t)
for i in range(0,length):
    k=2
    while (t[i][3]*k <= lastl):
        t.append((t[i][0]*k,t[i][1]*k,t[i][2]*k,t[i][3]*k))
        k+=1

        
t = sorted(t, key=itemgetter(3))       
print t 

for i in range(len(t)):
	if(t[i][3]<=1500000):
		a[t[i][3]]+=1
"""
         


sum=0
for i in range(len(asa)):
	if asa[i]==1:
		sum+=1

print sum
print asa.count(1)	
	