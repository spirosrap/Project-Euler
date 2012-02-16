def ispalindrome(x):
    string=str(x)
    if string==string[::-1]:
        return True
    else:
        return False

def largest_palindrome():
	pal = 0;
	mylist = [];
	for i in range(100,999):
		for j in range(100,999):
			pal=i*j;
			if(ispalindrome(pal)):
				mylist.append(pal)		
	mylist.sort();			
  	return mylist[len(mylist)-1];

print largest_palindrome();