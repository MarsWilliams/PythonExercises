#this function accepts two arguments, prints them out in a string, and then returns the result of the two arguments added.
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

#this function accepts two arguments, prints them out in a string, and then returns the result of the second argument subtracted from the first. 
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

#this function accepts two arguments, prints them in a string, and returns the result of multiplying the two together.
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
#this function accepts two arguments, prints them in a string, and returns the result of the first argument divided by the second argument
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

#prints a string
print "Let's do some math with just functions!"

#assigns variable to two arguments passed to the add function
age = add(30, 5)
#assigns variable to two arguments passed to the subtract function
height = subtract(78, 4)
#assigns variable to two arguments passed to the multiply function
weight = multiply(90, 2)
#assigns variable to two arguments passed to the divide function
iq = divide(100, 2)

#prints a string with four integer formatting specifiers that point to the variables add, height, weight, and iq
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#prints a string
print "Here is a puzzle."

#assigns a variable to functions passed arguments of functions

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?", True
