def twenty(n):
	m=n%20
	if m==1:
	  return "one";
	elif m==2:
	    return "two"
	elif m==3:
	    return "three"
	elif m==4:
	    return "four"
	elif m==5:
	    return "five"
	elif m==6:
	    return "six"
	elif m==7:
	    return "seven"
	elif m==8:
	    return "eight"
	elif m==9:
	    return "nine"
	elif m==10:
	    return "ten"
	elif m==11:
	    return "eleven"
	elif m==12:
	    return "twelve"
	elif m==13:
	    return "thirteen"
	elif m==14:
	    return "fourteen"
	elif m==15:
	    return "fifteen"
	elif m==16:
	    return "sixteen"
	elif m==17:
	    return "seventeen"
	elif m==18:
	    return "eighteen"
	elif m==19:
	    return "nineteen"
	else:
		return ""	
		
def decade(n):
	m=n%10
	if m==2:
	  return "twenty";
	elif m==3:
	    return "thirty"
	elif m==4:
	    return "forty"
	elif m==5:
	    return "fifty"
	elif m==6:
	    return "sixty"
	elif m==7:
	    return "seventy"
	elif m==8:
	    return "eighty"
	elif m==9:
		return "ninety"
	else:
		return ""
		
def hundred(n):
	if n<20:
		return twenty(n)
	elif n%10==0:
		return decade((n/10)%10)
	else:
		return decade(n/10) + twenty(n%10)
		
def thousand(n):
	if n<100:
		return hundred(n);
	elif n%100==0:
		return twenty(n/100) + "hundred"
	else:
		return twenty(n/100)+ "hundred"+"and"+ hundred(n%100)
		
		
		
					
			
print twenty(1);
print decade(3);
print hundred(43);
print thousand(142)
sum=0
for i in range(1,1000):
	sum+=len(thousand(i))
	print thousand(i)
print sum+len("onethousand")