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

def squares(n):
	s = 0
	while n:
		s += (n % 10) ** 2
		n=n//10
	return s


def sqDigCh(n):
	while n > 1 and n != 89 and n != 4:
		n = squares(n)
	return n>1

	
cache = [sqDigCh(i) for i in range(0,568)]
print cache

print "Answer to PE92 = ", sum(1 for i in range(10000000) if cache[squares(i)])
