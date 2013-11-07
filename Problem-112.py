def bouncy(n):
	number=str(n)
	check=int(number[0])
	direction=0
	for c in number[1:]:
		c=int(c)
		if direction==0:
			if c>check:
				direction=1
			elif c<check:
				direction=-1
		if direction==1:
			if c<check:
				return True
			elif c==check:
				direction==0
		if direction==-1:
			if c>check:
				return True
			if c==check:
				direction==0
		check=c				

	return False
	
sum=0
N=1770000
for i in range(100,N+1):
	if bouncy(i):
		sum+=1
	if (sum/float(i))==0.99:
		print i,sum/float(i)
			
print sum/float(N)		
