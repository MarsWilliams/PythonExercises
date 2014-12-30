#imports an argument variable from a Python module
from sys import argv

#assigns the argument variable to the name of the script and the name of the user
script, user_name = argv #requires you to enter two arguments when calling the file
#assigns the variable prompt to a symbol
prompt = '> '

#prints a string with two string formatting specifiers, pointing to user_name and the script name, respectively
print "Hi {}, I'm the {} script.".format(user_name, script) #trying new formatting module. Update: I dig it.
#prints a string
print "I'd like to ask you a few questions."
#prints a string with a string formatting specifier that points to user_name
print "Do you like me %s?" % user_name
#assigns the variable 'likes' to raw input from the user, prefaced by the information stored in the prompt variable
likes = raw_input(prompt)

#prints a string with a string formatting specifier that points to user_name
print "Where do you live %s?" % user_name 
#assigns the variable 'lives' to raw user input, prefaced by the information contained in the prompt variable
lives = raw_input(prompt)

#prints a string
print "What kind of computer do you have?"
#assigns the variable computer to raw user input, prefaced by the information stored in the prompt variable
computer = raw_input(prompt)

#prints a string with three raw input formatting specifiers that point to the variables 'likes,' 'lives,' and 'computer,' respectively
print """
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
