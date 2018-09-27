import sys

#for param in sys.argv[1:]:
#        print (param)

d = input()
d = d.replace('(', '[').replace(')', ']')
print(tuple(d))