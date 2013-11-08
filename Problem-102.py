from math import sqrt

def inside(p1,p2,p3):
    (p1x,p1y)=p1
    (p2x,p2y)=p2
    (p3x,p3y)=p3       
    (px,py)=(0,0)

    alpha = ((p2y - p3y)*(px - p3x) + (p3x - p2x)*(py - p3y))/float((p2y - p3y)*(p1x - p3x) + (p3x - p2x)*(p1y - p3y));
    beta = ((p3y - p1y)*(px - p3x) + (p1x - p3x)*(py - p3y))/float((p2y - p3y)*(p1x - p3x) + (p3x - p2x)*(p1y - p3y));

    gamma = 1.0 - alpha - beta;
    
    return (alpha>0 and beta>0 and gamma>0)
    
print inside((-340,495),(-153,-910),(835,-947))
print inside((-175,41),(-421,-714),(574,-645))   

M = [ [int(m) for m in s.split(',')] for s in open("triangles.txt")]
sum=0
for i in M:
    if inside((i[0],i[1]),(i[2],i[3]),(i[4],i[5])):
        sum+=1
        
print sum        