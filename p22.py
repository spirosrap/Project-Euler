import re

def get_grid(file_path):
    with open(file_path) as file:
        lines = file.read()
        
        grid = lines
        return grid
grid=get_grid("/Users/spirosrap/Desktop/names.txt")

myList = grid
myString =grid.split(",")


print myString[1][1:-1]
print myString[0][1:-1]

strings=[]
for i in range(0,len(myString)):
	strings.append(myString[i][1:-1])
		
strings.sort()
def numOfString(string):
	sum=0
	for i in range(0,len(string)):
		sum+=ord(string[i])-64
	return sum	
	
print numOfString("COLIN")
sum=0
for i in range(0,len(strings)):
	sum+=numOfString(strings[i])*(i+1)
		
print sum

