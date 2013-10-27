import math

g = [[int(n) for n in s.split(',')] for s in open('base_exp.txt').readlines()]
print g

f = []
for i in g:
	f.append(i[1]*math.log(i[0]))

	
print f.index(max(f))+1