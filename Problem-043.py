import itertools
import math
from math import *
import decimal
from decimal import *
from collections import deque
import prime


def pandigitalN(n):
	num=""
	for i in range(0,len(str(n))):
		num+=str(i+1)
		numbers=list(num)
		string=list(str(n))
		if(len(string)==len(str(n))):
			for i in range(0,len(numbers)):
				if numbers[i] in string:
					None
				else:
					return False
		else:
			return False
	return True

print



p=[]
st=""

def removeFromList(n,l):
	lis=[]
	for iL in range(0,len(l)):
			if(n == l[iL]):
				lis=l[:iL]+l[iL+1:]
	return lis			

ra1=[0,1,2,3,4,5,6,7,8,9]
sum=0
for d1 in range(0,10):
	ra2=removeFromList(d1,ra1)
	for d2 in ra2:
		ra3=removeFromList(d2,ra2)
		for d3 in ra3:
			ra4=removeFromList(d3,ra3)
			for d4 in ra4:
				ra5=removeFromList(d4,ra4)
				num1=int(str(d2)+str(d3)+str(d4))				
				if(num1%2==0):
					for d5 in ra5:
						ra6=removeFromList(d5,ra5)
						num2=int(str(d3)+str(d4)+str(d5))
						if(num2%3==0):
							for d6 in ra6:
								ra7=removeFromList(d6,ra6)
								num3=int(str(d4)+str(d5)+str(d6))
								if(num3%5==0):
									for d7 in ra7:
										ra8=removeFromList(d7,ra7)
										num4=int(str(d5)+str(d6)+str(d7))
										if(num4%7==0):
											for d8 in ra8:
												ra9=removeFromList(d8,ra8)
												num5=int(str(d6)+str(d7)+str(d8))												
												if(num5%11==0):
													for d9 in ra9:
														ra10=removeFromList(d9,ra9)
														num6=int(str(d7)+str(d8)+str(d9))												
														if(num6%13==0):
															for d10 in ra10:
																num7=int(str(d8)+str(d9)+str(d10))												
																if(num7%17==0):
																	print(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9)+str(d10))
																	sum+=int(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9)+str(d10))

print sum