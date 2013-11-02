from math import exp,pi,sqrt,log,pow	


p = [1]
def generate(n):
	for i in range(1, n + 1):
		s = 0
		k = 1
		while True:
			f = i - k * (3 * k - 1) / 2
			if f < 0:
				break
			if k % 2:
				s += p[f]
			else:
				s -= p[f]
			f = i - k * (3 * k + 1) / 2
			if f < 0:
				break
			if k % 2:
				s += p[f]
			else:
				s -= p[f]
			k+=1
		p.append(s)
		
generate(100000)
print p[100000]
for i in range(0,len(p)):
	if p[i]%1000000==0:
		print i

def gk(k):
	return k*(k*3-1)/2

def p(n):
	if n==0:
		return 1
	if n<0:
		return 0	
	k=1
	sum=0
	while True:
		sum+=pow(-1,k-1)*p(n-gk(k))
		sum+=pow(-1,k-1)*p(n-gk(-k))
		if (n-gk(k)<0 and n-gk(-k)<0):
			break
		k+=1
	return sum

#print p(20)
	
"""
N = 7000
ways = [1] + [0] * N

for i in xrange(1, N):
    for j in xrange(i, N+1):
        ways[j] = ways[j] + ways[j - i]

print ways[N]
print ways[5]

for i in range(i,N):
	if ways[N]%1000000==0:
		print N
"""
	
	