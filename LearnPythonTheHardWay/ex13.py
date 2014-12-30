#imports a argument variable from a Python module
from sys import argv

#unpacks the argument variable, and assigns it to four variables
script, first, second, third = argv

first = raw_input("What would you like the first argument to be?")
#prints a string followed by the name of the script
print "The script is called:", script
#prints a string followed by the name of the first argument
print "Your first variable is:", first
#prints a string followed by the name of the second argument
print "Your second variable is:", second
#prints a string followed by the name of the third argument
print "Your third variable is:", third
