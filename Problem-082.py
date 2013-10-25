g = [[int(n) for n in s.split(',')] for s in open('matrix.txt').readlines()]
N=len(g)
matrix = {(a,b):g[a][b] for a in xrange(N) for b in xrange(N)}

def minpath2(matrix,start,end,mindistance):
    dist = {(a,b):10**6 for a in xrange(N) for b in xrange(N)}
    dist[start] = matrix[start]
    Q = [(a,b) for a in xrange(N) for b in xrange(N)]
    keys = matrix.keys()
    while len(Q):
        mi = 10**6
        u = start
        for key in Q:
            if dist[key] < mi:
                u,mi = key,dist[key]
        Q.remove(u)
        if u == end: break
        
        if(u[1]==0):
        	neighbors = [(u[0],u[1]+1)]
        elif(u[1]==N-1):
        	neighbors=[]
        else:
	        neighbors = [(u[0]+1, u[1]),(u[0],u[1]+1),(u[0]-1,u[1])]
        #print u
        for v in neighbors:
            if v not in keys: continue
            alt = dist[u] + matrix[v] 
            if alt < dist[v]:
                dist[v] = alt
                #print dist[v]
        #print "---------"
    d=[]    
    for i in xrange(N):
    	d.append(dist[i,N-1])                                
    return d

mindist=10**6
minis=[]
for i in xrange(N):
	m = min(minpath2(matrix,(i,0),(N-1,N-1),mindist))
	print m
	minis.append(m)
	
print min(minis)