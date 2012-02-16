def difference():
	count1=0;
	count2=0;
	for i in range(1,101):
		count1+=i*i;
		count2+=i;
	return count2*count2-count1;

print difference();