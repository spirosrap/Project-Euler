import itertools
import math
import decimal
from decimal import *
from collections import deque
import prime

sum=0
for p100 in range(0,3):
	for p50 in range(0,5-2*p100):
		for p20 in range(0,11-5*p100-2*p50):
			for p10 in range(0,21-p100*10-p50*5-p20*2):
				for p5 in range(0,41-p100*20-p50*10-p20*4):
					for p2 in range(0,101-p100*50-p20*10-25*p50):
						for p1 in range(0,201-p100*100-p50*50-p20*20-p10*10-p5*5-p2*2):
							if(100*p100+50*p50+20*p20+10*p10+5*p5+2*p2+1*p1==200):
								sum+=1
							
print sum