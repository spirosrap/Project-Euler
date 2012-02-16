from decimal import *

getcontext().prec = 5

for a in range(1,10):
	for b in range(1,10):
		for c in range(1,10):
			for d in range(1,10):
				example=Decimal(a*10+b)/Decimal(c*10+d)
				if(b==d):
					example1=Decimal(a)/Decimal(c)
					if(example<1 and (example==example1)):
						print str(example),str(a)+str(b),str(c)+str(d)					
				if(b==c):
					example2=Decimal(a)/Decimal(d)
					if(example<1 and (example==example2)):
						print str(example),str(a)+str(b),str(c)+str(d)					
				if(a==d):
					example3=Decimal(b)/Decimal(c)
					if(example<1 and (example==example3)):
						print str(example),str(a)+str(b),str(c)+str(d)					
				if(a==c):
					example4=Decimal(b)/Decimal(d)
					if(example<1 and (example==example4)):
						print str(example),str(a)+str(b),str(c)+str(d)													