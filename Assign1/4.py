import random
ran = random.randint(1,100)
flag = 0
count1 = 0
while flag == 0 and count1 <= 9:
	count1 +=1
	uguess = int(input("Enter guess"))
	if ran > uguess:
		print "number is greater"
	elif ran < uguess:
		print "number is smaller"
	elif ran == uguess:
		print "Congratulations!!!!!!"
		print "You choose correct number in", count1,"attempt"
		flag = 1

if flag==0 and count1==10:
	print "Sorry! You have not guess the number"
