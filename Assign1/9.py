count = 0
i = 1
while count < 10:
	sum1 = 0
	divisor = 0
	for j in range(1,i+1):
		if(i % j == 0):
			sum1 +=  1.0/j
			divisor += 1
	val = divisor/sum1
	valint = int(val)
	if val == valint:
		count+=1
		print i

	i=i+1

