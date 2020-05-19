fob = open("/etc/hosts","r+")
content = fob.read()
redirect = "127.0.0.1"
website = "www.amazon.com"
if website in content:
	print "pass"
else :
	fob.write(redirect + " " + website + "\n") 
fob.close()
