import sys

myline = open(sys.argv[1], "r")
myline = myline.read().split("\n")
dct = {}
for i in myline:
    i = i.split(":")
    dct[i[0]] = i[1:]

trying = sys.argv[2].split(",")
try:
    for i in trying:
        print(f"Name: {i} University: {str(dct[i])[1:-1]}")
except KeyError:
    print(f"No record of {i} was found!")