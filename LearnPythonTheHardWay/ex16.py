#imports package containing the list argv
from sys import argv

#assigns two values to argv, the script and the filename
script, filename = argv

#prints a string with a raw input formatting specifier that points to the file name.
print "We're going to erase %r." % filename
#prints a string
print "If you don't want that, hit CTRL-C (^C)."
#prints a string
print "If you do want that, hit RETURN."

#requests input from the user
raw_input("?")

#prints a string
print "Opening the file..."
#assigns a variable to an action
target = open(filename, 'w')

#prints a string
print "Now I'm going to ask you for three lines."

#Requests user input for three lines of the script
line1, line2, line3 = raw_input("line 1: "), raw_input("line 2: "), raw_input("line 3: ")

#prints a string
print "I'm going to write these to the file."

#overwrites the script with the user-inputted lines.
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#prints a string
print "And finally, we close it."
#closes the file
target.close()
