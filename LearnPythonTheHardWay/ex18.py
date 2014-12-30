#takes an unknown number of arguments, assigns two arguments to args (arbitrarily), and then prints them out.
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#takes two arguments and prints those arguments in a string
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
#takes one argument and prints that argument in a string
def print_one(arg1):
    print "arg1: %r" % arg1

#takes one argument and prints that argument in a string
def print_none():
    print "I got nothing."

#prints the resuls of calling each function with given arguments
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
