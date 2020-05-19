lower = int(input("Enter lower"))
upper = int(input("Enter upper"))
for i in range(lower,upper+1):
	sum = 0
	num = i
	a = i
	num = i
	count = 0
	while a > 0:
		count = count+1
		a = a/10
                
	while i > 0:
		digit = i % 10
		sum += digit ** count
		i = i / 10
	if num == sum:
		print num 

