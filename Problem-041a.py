p1 = Prime()




p=[]
st=""

def removeFromList(n,l):
	lis=[]
	for iL in range(0,len(l)):
			if(n == l[iL]):
				lis=l[:iL]+l[iL+1:]
	return lis			
ra1=[1,2,3,4,5,6,7,8,9]
for i1 in ra1:
	ra2=removeFromList(i1,ra1)
	for i2 in ra2:
		ra3=removeFromList(i2,ra2)
		for i3 in ra3:
			ra4=removeFromList(i3,ra3)
			for i4 in ra4:
				ra5=removeFromList(i4,ra4)
				for i5 in ra5:
					ra6=removeFromList(i5,ra5)
					for i6 in ra6:
						ra7=removeFromList(i6,ra6)
						for i7 in ra7:
							ra8=removeFromList(i7,ra7)
							for i8 in ra8:
								ra9=removeFromList(i8,ra8)
								for i9 in ra9:
									st=str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)+str(i9)
									if(p1.factor(int(st))==None):
										p.append(st)
						
	
print p