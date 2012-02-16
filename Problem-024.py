import itertools
perms = list(itertools.permutations('0123456789'))
perms.sort()
print perms[0]
print perms[1]		
print perms[2]

def tupleToStr(t):
	i=0
	s=""
	while(i<len(t)):
		s+=str(t[i])
		i+=1
	return s
permute=[]

print tupleToStr(perms[999999])