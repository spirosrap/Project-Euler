import calendar

print calendar.monthrange(2012, 2)
sum=0
for year in range(1901,2001):
	for month in range(1,13):
		if(calendar.monthrange(year,month)[0]==6):
			print year
			print month
			sum+=1
			print calendar.monthrange(year,month)

print sum