#prints a string
print "How old are you?",
#assigns a variable to raw user input
age = raw_input()
#prints a string
print "How tall are you?",
#assigns a variable to raw user input
height = raw_input()
#prints a string
print "How much do you weigh?",
#assigns a variable to raw user input
weight = raw_input()

#prints a string with raw data formatting specifiers that point to information stored in variables
print """So, you're %r old, %r tall and %r heavy.""" % (age, height, weight)

print "What is your name?"
name = raw_input().capitalize
print "Hello %r! It's so nice to meet you." % (name)
print "Did you have a good weekend? What did you do?"
activities = raw_input().lowercase
print "Wow, really? You %? How fun!" % (activities)
print "I like you %. Let's % together some time." % (name, activities)
