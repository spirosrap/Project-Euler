#!/usr/bin/python
import re
import math
from math import *
import itertools
import decimal
from decimal import *
from collections import deque
from prime import Prime
import operator
import string
from sets import Set

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

p=[]
nom1=3
den1=7
nom=2
den=5
while(den+den1<=1000000):
	nom=nom+nom1
	den=den+den1

print nom,den

				
p.sort()			
print p
		
