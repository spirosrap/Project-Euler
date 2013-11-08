from math import sqrt
"""
for i1 in range(1,11):
    for i2 in range(1,11):
        for i3 in range(1,11):
            for i4 in range(1,11):          
                for i5 in range(1,11):
                    for i6 in range(1,11):
                        for i7 in range(1,11):
                            for i8 in range(1,11):
                                for i9 in range(1,11):
                                    string="1"+str(i1)+"2"+str(i2)+"3"+str(i3)+"4"+str(i4)+"5"+str(i5)+"6"+str(i6)+"7"+str(i7)+"8"+str(i8)+"9"+str(i9)+"0"
                                    a = sqrt(int(string))
                                    if (a == int(a)):
                                        print string
"""

#The square of any number, n, will end in 00 if the last digit of n is zero.  
#So, our square root ends in a zero and the square has the form  1_2_3_4_5_6_7_8_900.

max = int(sqrt(19293949596979899))+1

print max
def valid(n):
    a=str(n)
    if(a[0]=="1" and a[2]=="2" and a[4]=="3" and a[6]=="4" and a[8]=="5" and a[10]=="6" and a[12]=="7" and a[14]=="8" and a[16]=="9"):
        return True
    else:
        return False

print valid(10203040506070809)        



for i in xrange(max+1,-1,-1):
    if valid(i*i):
        print i    