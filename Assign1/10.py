a = float(input("Enter a starting number\n"))
r  = float(input("Enter a common ratio"))
i = 0
print "Geometric series starting with{", a ,"} and with comman difference of {" , r , "} is:"
for i in range(10):
    print(a)
    a = a * r

