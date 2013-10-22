#!/usr/bin/python
import math
from math import *
import itertools
import decimal
from decimal import *
from collections import deque
from prime import Prime

def get_grid(file_path):
    with open(file_path) as file:
        lines = file.read()
        grid=""        
        grid += lines
        return grid
grid=get_grid("/Users/spirosrap/Dropbox/poker.txt")

myList = grid
i=0
hands=[]
while(i<len(myList)):
	while(myList[i]!="\n"):		
		hands.append(myList[i:i+2])
		i+=3
	i+=1
"""	
print hands[0:5],hands[5:10]
print hands[0],hands[1],hands[2],hands[3],hands[4]
print hands[0][0]
"""
def tupleToStr(t):
	i=0
	s=""
	while(i<len(t)):
		s+=str(t[i])
		i+=1
	return s

def isPerm(n1,n2):
	permsN1=list(itertools.permutations(str(n1)))
	size=len(permsN1)
	perms=[]
	for i in range(0,size):
		perms.append(str(tupleToStr(permsN1[i])))
	if(n2 in perms):
		return True
		
def valuesList(values):
	lis=[]
	for i in range(0,len(values)):
		if(values[i]=="T"):
			lis.append(10)
		elif(values[i]=="J"):
			lis.append(11)
		elif(values[i]=="Q"):
			lis.append(12)
		elif(values[i]=="K"):
			lis.append(13)
		elif(values[i]=="A"):
			lis.append(14)
		else:
			lis.append(int(values[i]))
	lis.sort()
	return lis

def checkHand(hand):
	#Royal Flush
	sameSuit = hand[0][1]==hand[1][1] and hand[1][1]==hand[2][1] and hand[2][1]==hand[3][1] and hand[3][1]==hand[4][1]
	values = valuesList(hand[0][0]+hand[1][0]+hand[2][0]+hand[3][0]+hand[4][0])
	values1 = hand[0][0]+hand[1][0]+hand[2][0]+hand[3][0]+hand[4][0]
	
	if(values[1]==values[0]+1 and values[2]==values[0]+2 and values[3]==values[0]+3 and values[4]==values[0]+4):
		if sameSuit:
			if values[0]==10:
				return (5000000,"Royal Flush")
			else:
				return (400000*values[4],"Straight Flush")
		else:
			return (15000*values[4],"Straight")

	if(values[0:4]==4*[values[0]]): 
		return (3000*values[0]+values[4],"Four of a Kind")
	if(values[1:5]==[4*values[1]]):
		return (3000*values[4]+values[0],"Four of a Kind")
								
	if(sameSuit):
		return (2000,"Flush")
	
	if((values[0]==values[1] and values[2:5]==[values[2]]*3) or (values[3]==values[4] and values[0:3]==[values[0]]*3)):
		return (2500,"Full House")
		
	if values[0:3]==3*[values[0]] or values[1:4]==3*[values[1]] or values[2:5]==3*[values[2]] :
			return (1400,"Three of a Kind")
							
	if (values[0:2]==2*[values[0]] and values[2:4]==2*[values[2]]) or (values[1:3]==2*[values[1]] and values[3:5]==2*[values[3]]) or (values[0:2]==2*[values[0]] and values[3:5]==2*[values[3]]):
		return (1300,"Two Pairs")

	if values[0:2]==2*[values[0]]:
		return (15*values[0]+max(values[2:5]),"One Pair")
	if values[1:3]==2*[values[1]]:
			return (15*values[1]+max([values[0],values[3],values[4]]),"One Pair")
	if values[2:4]==2*[values[2]]:
		return (15*values[2]+max([values[0],values[1],values[4]]),"One Pair")
	if values[3:5]==2*[values[3]]:
		return (15*values[3]+max([values[0],values[1],values[2]]),"One Pair")


	return (max(values),"Maximum Hand")	
		
			
i=0
sum=0
while(i<len(hands)):
	h1=checkHand(hands[i:i+5])
	h2=checkHand(hands[i+5:i+10])
	
	if h1[0]>h2[0]:	
		sum+=1
	print hands[i:i+5],h1[1],hands[i+5:i+10],h2[1],h1[0]-h2[0]		
	i+=10
print sum
