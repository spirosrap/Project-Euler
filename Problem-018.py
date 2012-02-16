def get_grid(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        
        grid = [[int(c) for c in l.split(" ")] for l in lines]
        return grid
grid=get_grid("/Users/spirosrap/Desktop/triangle.txt")

class tree_node:
	value=0
	
	def __init__(self,leftParent,rightParent,n):
		if leftParent==None:
			leftValue=0
		else:
			leftValue = leftParent.value
			
		if rightParent==None:
			rightValue=0
		else:
			rightValue=rightParent.value
			
		self.value = n +max(leftValue,rightValue)
def get_max_tree_node_path(grid):
  branches=[]		
  for rowIndex in xrange(0, len(grid), 1):
  	branch=[]
	row = grid[rowIndex]
	for columnIndex in xrange(0,len(row),1):
		leftParent,rightParent = None,None
		if rowIndex>0:
			parentBranch = branches[rowIndex-1]
			if columnIndex <len(row) -1:
			  rightParent = parentBranch[columnIndex]
			
			if columnIndex > 0:
				leftParent = parentBranch[columnIndex-1]
		node = tree_node(leftParent,rightParent,row[columnIndex])
		branch.append(node);
	branches.append(branch);
  return  max(n.value for n in branches[-1])

print get_max_tree_node_path(grid)