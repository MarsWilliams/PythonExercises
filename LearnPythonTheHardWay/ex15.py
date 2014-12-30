#imports from a python package the list of command-line arguments passed to the script
from sys import argv

#finds a filename with the list
script, filename = argv

#assigns a variable to the action of opening a specific file
txt = open(filename)

#prints a string with raw data formatting that points to the file assigned to txt
print "Here's your file %r:" % filename
#prints the content (file object) of the file that is assigned to txt
print txt.read()

close(txt)

#prints a string
print "Type the filename again:"
#assigns a variable to raw inpur from the user
file_again = raw_input("> ")

#assigns a variable to the action of opening the user-defined file name
txt_again = open(file_again)

#prints the content (file object) of the user-defined file
print txt_again.read()

close(txt_again)
