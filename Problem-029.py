import math
tabl=[]
fout = open("/Users/spirosrap/Desktop/output.dat", "w")

for a in range(2,101):
	for b in range(2,101):
		if(a**b) in tabl:
			None
		else:
			tabl.append(a**b)
			fout.write(str(a**b)+" ")

tabl.sort()
print tabl,len(tabl)