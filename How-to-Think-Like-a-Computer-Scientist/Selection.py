Exercise 1
#Recreate code to see how expressions evaluate
3 == 3
3 != 3
3 >= 4
not (3 < 4)
#output
#True
#False
#False
#False

Exercise 2
#Give the logical opposites of these conditions. You are not allowed to use the not operator.
#a > b
#a >= b
#a >= 18  and  day == 3
#a >= 18  or  day != 3
a < b
a <= b
a <= 18 and day != 3
a <= 18 or day == 3

Exercise 3
#Write a function which is given an exam mark, and it returns a string — the grade for that mark 
#requests user input for mark
mark = int(input("What mark did you get on your assignment?")
#defines grade translation function using boolean expressions
def grade(mark):
    if mark >= 90:
        return "You recieved an A on your assignment. Bravo!"
    else:
        if mark >= 80:
            return "You recieved a B on your assignment. Good job."
        else:
            if mark >= 70:
                return "You recieved a C on your assignment. Way to crest the bell curve!"
            else:
                if mark >= 60:
                    return "You recieved a D on your assignment. What happened?"
                else:
                    return "You recieved an F on your assignment. Epic FAIL."
#calls the function and passes it mark, requests it to print outcome
print grade(mark)

Exercise 4
#Modify the turtle bar chart program from the previous chapter so that the bar for any value of 200 or more is filled with red, values between [100 and 200) are filled yellow, and bars representing values less than 100 are filled green.
import turtle

#define bar drawing function
def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

xs = [48,117,200,240,160,260,220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.setworldcoordinates(0-border,0-border,40*numbars+border,maxheight+border)

#modified loop to include fill color selection based on value
for a in xs:
    if a >= 200:
        tess.fillcolor("red")
        drawBar(tess, a)
    elif a >= 100:
        tess.fillcolor("yellow")
        drawBar(tess, a)
    else:
        tess.fillcolor("green")
        drawBar(tess, a)

wn.exitonclick()

Exercise 5
#In the turtle bar chart program, what do you expect to happen if one or more of the data values in the list is negative? Go back and try it out. Change the program so that when it prints the text value for the negative bars, it puts the text above the base of the bar (on the 0 axis).
import turtle
#modified drawbar function to format for negative data values
def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    if height > 0:
        t.forward(height)
        t.write(str(height))
    else:
        t.write(str(height))
        t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape



xs = [-48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)


for a in xs:
    if a >= 200:
        tess.fillcolor("red")
        drawBar(tess, a)
    elif a >= 100:
        tess.fillcolor("yellow")
        drawBar(tess, a)
    else:
        tess.fillcolor("green")
        drawBar(tess, a)

wn.exitonclick()

Exercise 6
#Write a function findHypot. The function will be given the length of two sides of a right-angled triangle and it should return the length of the hypotenuse. (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)
from test import testEqual

def findHypot(a, b):
    import math
    return math.hypot(a, b)

testEqual(findHypot(12.0, 5.0), 13.0)
testEqual(findHypot(14.0, 48.0), 50.0)
testEqual(findHypot(21.0, 72.0), 75.0)
testEqual(findHypot(1, 1.73205), 1.999999)

Exercise 7
#Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.
from test import testEqual

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
testEqual(is_even(10), True)
testEqual(is_even(5), False)
testEqual(is_even(1), False)
testEqual(is_even(0), True)

Exercise 8
#Now write the function is_odd(n) that returns True when n is odd and False otherwise.
from test import testEqual

def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)

Exercise 9
#Modify is_odd so that it uses a call to is_even to determine if its argument is an odd integer.
from test import testEqual

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def is_odd(n):
    if is_even(n) == True:
        return False
    else:
        return True

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)

Exercise 10
#Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.
#Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as
#if  abs(x - y) < 0.001:      # if x is approximately equal to y
from test import testEqual

def is_rightangled(a, b, c):
    if abs((a**2 + b**2)-c**2) < 0.001:
        return True
    else:
        return False

testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 8.0, 16.0), False)
testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.4, 0.64031), True)

Exercise 11
#Extend the above program so that the sides can be given to the function in any order.
from test import testEqual

def is_rightangled(a, b, c):
    if c > a and c > b:
        if abs((a**2 + b**2)-c**2) < 0.001:
            return True
        else:
            return False
    else:
        if b > c and b > a:
            if abs((a**2 + c**2)-b**2) < 0.001:
                return True
            else:
                return False
        else:
            if a > c and a > b:
                if abs((b**2 + c**2)-a**2) < 0.001:
                    return True
                else:
                    return False
                
testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(16.0, 4.0, 8.0), False)
testEqual(is_rightangled(4.1, 9.1678787077, 8.2), True)
testEqual(is_rightangled(9.16787, 4.1, 8.2), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.64031, 0.4), True)
