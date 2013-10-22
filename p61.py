n=0
triangle=[]
square=[]
pentagonal=[]
hexagonal=[]
heptagonal=[]
octagonal=[]
nums=[]
while(n<=10000):		
	t=n*(n+1)/2
	if(t>=1000 and t<=10000):
		triangle.append(str(t))
	t=n*n
	if(t>=1000 and t<=10000):
		square.append(str(t))
	t=n*(3*n-1)/2
	if(t>=1000 and t<=10000):
		pentagonal.append(str(t))
	t=n*(2*n-1)
	if(t>=1000 and t<=10000):
		hexagonal.append(str(t))	
	t=n*(5*n-3)/2
	if(t>=1000 and t<=10000):
		heptagonal.append(str(t))
	t=n*(3*n-2)	
	if(t>=1000 and t<=10000):
		octagonal.append(str(t))
	n+=1
	
nums=[]
nums.append(triangle)
nums.append(square)
nums.append(pentagonal)
nums.append(hexagonal)
nums.append(heptagonal)
nums.append(octagonal)
a=triangle
b=square
c=pentagonal
d=hexagonal
e=heptagonal
f=octagonal

for i in a:
	set = [b, c, d, e, f]
	for j in set:
		for k in j:
			if (k[0] == i[2] and k[1] == i[3]):
				set = [b, c, d, e, f]
				set.remove(j)
				for l in set:
					for m in l:
						if (m[0] == k[2] and m[1] == k[3]):
							set = [b, c, d, e, f]
							set.remove(j)
							set.remove(l)
							for n in set:
								for o in n:
									if (o[0] == m[2] and o[1] == m[3]):
										set = [b, c, d, e, f]
										set.remove(j)
										set.remove(l)
										set.remove(n)
										for p in set:
											for q in p:
												if (q[0] == o[2] and q[1] == o[3]):
													set = [b, c, d, e, f]
													set.remove(j)
													set.remove(l)
													set.remove(n)
													set.remove(p)
													for r in set:
														for s in r:
															if (s[0] == q[2] and s[1] == q[3] and s[2] == i[0] and s[3] == i[1]):
																print i, k, m, o, q, s
