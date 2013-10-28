import math
a=[]
for x in range(1,2000):
	for y in range(1,2000):
		sum=(x*x+x)*(y*y+y)/4
		if sum==1999998:
			print x*y
			