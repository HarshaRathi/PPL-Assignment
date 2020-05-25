import sys
try:
    print("Enter a filename : ")
    filename = input()
    f = open(filename,"r")
    read = int(f.read())
    print(read)
    f.close()
except IOError as err:
    print("IO error: {0}".format(err))
except OSError as err:
    print("OS error: {0}".format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
    