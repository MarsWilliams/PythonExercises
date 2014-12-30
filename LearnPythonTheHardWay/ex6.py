#assigns variable x to a string with integer formatting
x = "There are %d types of people." % 10
#assigns variable binary to a string
binary = "binary"
#assigns variable do_not to a string
do_not = "don't"
#assigns variable y to a string with string formatting
y = "Those who know %s and those who %s." % (binary, do_not) #2 strings inside a string

#prints x
print x
#prints y
print y

#prints a string with x subbed for raw data formatting
print "I said: %r." % x #string (raw data) inside a string
#prints a string with y subbed for string formatting
print "I also said: '%s'." % y #string inside a string

#assigns the variable hilarious to the Boolean False
hilarious = False
#assigns the variable joke_evaluation to a string with raw data formatting
joke_evaluation = "Isn't that joke so funny?! %r" #string (raw data) inside a string

#prints joke_evaluation followed by hilarious
print joke_evaluation % hilarious

#assigns w to a string
w = "This is the left side of..."
#assigns e to a string
e = "a string with a right side."

#prints w and e concatenated 
print w + e
