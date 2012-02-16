for n in range(1,350):
	for m in range(1,350):
		sum=2*(m*m+m*n);
		if sum==1000:
			a = m*m-n*n
			b = 2*m*n
			c = m*m+n*n
			print a*b*c			
