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

L = 12000+1
c = 0
for n in range(5, L):
  for k in range(n/3 + 1, (n-1)/2 + 1):
    if gcd(n,k) == 1: c+=1

print c