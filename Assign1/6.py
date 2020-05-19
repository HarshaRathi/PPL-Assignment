i = 0;
count = 0;
while count < 10:
	sum1 = 0

	sum2 = 0
	
	for k in range(1,i):
		if(i%k==0):
			sum1+=k
	
	for p in range(1,sum1):
		if(sum1%p==0):
			sum2+=p
	
	if sum2 == i and sum1>sum2:
		count+=1
		print sum1,sum2
	
	i+=1
		+
