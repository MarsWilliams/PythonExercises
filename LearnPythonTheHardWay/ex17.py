#imports an argument variable from a Python module
from sys import argv

#import from an os module a function that checks the existence of a file
from os.path import exists

#assigns three variables to argv
script, from_file, to_file = argv

#prints a string with two string formatting specifiers that refer to two of the variables contained in argv
print "Copying from %s to %s" % (from_file, to_file)

#assigns a function (opening a file and reading, then printing, its content) to the variable indata
in_file = open(from_file).read()

#prints a string that contains an integer formatting specifier that points to the length of the file (as read)
print "The input file is %d bytes long" % len(in_file)

#prints a string followed by a raw data formatting specifier that points to the file, as evaluated by the exists function
print "Does the output file exist? %r" % exists(to_file)
#prints a string
print "Ready, hit RETURN to continue, CTRL-C to abort."
#accepts user input
raw_input()

#assigns a function (opening a file and writing the contents of the other file, as a string, in it)
out_file = open(to_file, 'w').write(in_file)

#prints a string
print "Alright, all done."

#closes both of the files
out_file.close()
in_file.close()
