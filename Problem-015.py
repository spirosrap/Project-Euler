routesH=[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
routesV=1;
routesCurrent=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

for j in range(0,20):
  for i in range(0,21):
	  if(i==0):
		routesCurrent[0]=1;
	  else:
	    routesCurrent[i] = routesCurrent[i-1]+routesH[i]
  routesH=routesCurrent;
  routesV=1;
print routesCurrent[20]

