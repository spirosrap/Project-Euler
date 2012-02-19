import itertools
import math
from math import *
import decimal
from decimal import *
from collections import deque
import prime
from string import ascii_uppercase

def get_grid(file_path):
    with open(file_path) as file:
        lines = file.read()
        
        grid = lines
        return grid
grid=get_grid("/Users/spirosrap/Desktop/words.txt")

myList = grid
myString =grid.strip('"').split(",")

words=[]
words.append(myString[0][2:-1])
for i in range(1,len(myString)-1):
	words.append(myString[i][1:-1])
words.append(myString[len(myString)-1][1:-2])

print words

def letter_value(letter):
    return ascii_uppercase.index(letter.upper())+1

def triangle(n):
	return int((0.5) * n * (n+1))
triangles=[]	
for i in range(1,50):
	triangles.append(triangle(i))
		
print letter_value("A")	
sums=0
for word in words:	
	sum=0
	for i in range(0,len(word)):		
		sum+=letter_value(str(word[i]))
	if(sum in triangles):
		sums+=1

print sums