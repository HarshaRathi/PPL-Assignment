
a = list(range(1,26))
b = list()
c = raw_input("Enter Page Number")
for i in c.split():
	b.append(int(i))
d = set(a) - set(b)
print ("Missing Page Numbers are")
print d


