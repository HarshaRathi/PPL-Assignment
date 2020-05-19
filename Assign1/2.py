import random
num = raw_input("Do you want to play?(y/n)")
while num == "y":
	ran = random.randint(1,6)
	print ran
	num = raw_input("Do you want to continue?(y/n)")
print "End Rolling The Dice"


