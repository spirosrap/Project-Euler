import itertools
import math
import decimal
from decimal import *
from collections import deque
import prime

string=""
for i in range(1,1000001):
	string+=str(i)

lstr=list(string)

print int(lstr[0])*int(lstr[9])*int(lstr[99])*int(lstr[999])*int(lstr[9999])*int(lstr[99999])*int(lstr[999999])