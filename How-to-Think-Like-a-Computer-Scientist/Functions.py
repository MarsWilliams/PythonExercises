Exercise 1
#Use the drawsquare function we wrote in this chapter in a program to draw the image shown below. Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)
#import turtle
import turtle

#create function for drawing a square
def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

#set up turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")

#create loop to use the drawSquare function to draw 5 independent squares
for i in range(5):
    drawSquare(alex,20)
    alex.penup()
    alex.forward(40)
    alex.pendown()

#exit on click 
wn.exitonclick()

Exercise 2
#import turtle
import turtle

#create function for drawing a square
def drawSquare(t, si, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(si):
        t.forward(sz)
        t.left(90)
        t.forward(20)
        

#set up turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")

#create loop to use the drawSquare function to draw 5 independent squares
growth = 1
for i in range(5):
    drawSquare(alex, 4, (20 * growth))
    alex.penup()
    alex.right(180)
    alex.forward(10)
    alex.left(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()
    growth += 1

#exit on click 
wn.exitonclick()

Exercise 3
#set up turtle
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("pink")

#create function to draw polygon
def drawPoly(someturtle, somesides, somesize):
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360/somesides)

#call function
drawPoly(tess, 8, 50)    

#exit on click
wn.exitonclick()

Exercise 4
#Draw this pretty pattern. (See result of my code to see the pattern :D)
#set up turtle
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
ben = turtle.Turtle()
ben.color("blue")

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

for i in range(20):
        drawSquare(ben, 40)
        ben.penup()
        ben.left(360/20)
        ben.pendown()
 
wn.exitonclick()

Exercise 5
#The two spirals in this picture differ only by the turn angle. Draw both.
#Spiral 1
#set up turtle
import turtle
ben = turtle.Turtle()
ben.color("blue")
wn = turtle.Screen()
wn.bgcolor("lightgreen")

#create function that accepts three arguments and draws an expanding, unfinished, square
def pyramida(turtle, number_sides, length_side, angle):
    expansion_counter = 1
    while True:
        for i in range(number_sides):
            turtle.right(90)
            turtle.forward(length_side * expansion_counter)
            turtle.right(angle)
            expansion_counter += 1
        if expansion_counter > 30:
           break
            
#position ben
ben.penup()
ben.backward(80)
ben.pendown()

pyramida(ben, 4, 2, 0) #Creates first spiral

#position ben
ben.home()
ben.penup()
ben.forward(160)
ben.pendown()

pyramida(ben, 4, 2, 5) #Creates second spiral

wn.exitonclick()

Exit 6
#Write a non-fruitful function drawEquitriangle(someturtle, somesize) which calls drawPoly from the previous question to have its turtle draw a equilateral triangle.
#set up turtle
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
ben = turtle.Turtle()
ben.color("blue")

#Create polygon function that takes three arugments
def drawPoly(someturtle, somesides, somesize):
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360/somesides)

#create equilateral triangle function that calls the polygon function, and gives it a value of 3 for the variable somesides        
def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)
    
drawEquitriangle(ben, 13)

Exercise 7
Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n. So sumTo(10) would be 1+2+3...+10 which would return the value 55. 
from test import testEqual
sum_group = []
def sumTo(n):
    counter = 1
    for i in range(n):
        sum_group.append(counter)
        counter += 1
    return sum_group

print(sum(sumTo(10)))

or 

from test import testEqual
def sumTo(n):
    sum_group = n * (n + 1) / 2
    return sum_group

print(int(sumTo(10)))

Exercise 8
#Write a function areaOfCircle(r) which returns the area of a circle of radius r. Make sure you use the math module in your solution.
from test import testEqual
import math

def areaOfCircle(r):
    
    a = (r**2)*math.pi
    return a

t = areaOfCircle(0)
testEqual(t,0)
t = areaOfCircle(1)
testEqual(t,math.pi)
t = areaOfCircle(100)
testEqual(t,31415.926535897932)


Exercise 9
#Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units.
#set up turtle
import turtle
ben = turtle.Turtle()
ben.color("blue")
wn = turtle.Screen()
wn.bgcolor("lightgreen")

#create funciton to draw star, taking one argument
def drawStar(t):
    for i in range(5):
        t.right(216)
        t.forward(100)

#call function        
drawStar(ben)

Exercise 10
#Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right by 144, put the pen down, and draw the next star. You’ll get something like this (note that you will need to move to the left before drawing your first star in order to fit everything in the window):
import turtle
ben = turtle.Turtle()
ben.color("hotpink")
wn = turtle.Screen()
wn.bgcolor("lightgreen")

def drawStars(t):
    for i in range(5):
        t.forward(100)
        t.left(216)
        
ben.home()
ben.penup()
ben.left(90)
ben.forward(20)
ben.left(90)
ben.forward(175)
ben.left(180)

ben.pendown()

for i in range(5):
    drawStars(ben)        
    ben.penup()
    ben.forward(350)
    ben.right(144)
    ben.pendown()

Exercise 11
#Extend the star function to draw an n pointed star. (Hint: n must be an odd number greater or equal to 3).
import turtle
ben = turtle.Turtle()
ben.color("hotpink")
wn = turtle.Screen()
wn.bgcolor("lightgreen")

def drawStar(t, s):
    if (s%2 == 0) or (s < 3):
        print("You must choose an odd number that is greater than or equal 3.") 
    else:    
        for i in range(s):
            t.forward(100)
            t.left(180 - 180/s)

drawStar(ben, 3)

Exercise 12
#Write a function called drawSprite that will draw a sprite. The function will need parameters for the turtle, the number of legs, and the length of the legs. Invoke the function to create a sprite with 15 legs of length 120.
import turtle
ben = turtle.Turtle()
ben.color("SlateGray")
wn = turtle.Screen()
wn.bgcolor("LightSalmon ")

def drawSprite(some_turtle, some_number_legs, some_length_legs):
    some_turtle.shape("circle")
    some_turtle.stamp()
    for i in range(some_number_legs):
        some_turtle.forward(some_length_legs)
        some_turtle.stamp()
        some_turtle.penup()
        some_turtle.backward(some_length_legs)
        some_turtle.pendown()
        some_turtle.left(360/some_number_legs)
        some_turtle.pendown()

drawSprite(ben, 15, 120)

Exercise 13
#Rewrite the function sumTo(n) that returns the sum of all integer numbers up to and including n. This time use the accumulator pattern.
from test import testEqual
sum_group = []
def sumTo(n):
    counter = 1
    for i in range(n):
        sum_group.append(counter)
        counter += 1
    return sum(sum_group)

print(sumTo(5))

Exercise 14
def mySqrt(n, guesses):
    oldguess = 0.5 * n
    newguess = 0.5 * (oldguess + n/oldguess)
    for i in range(guesses):
        newguess = 0.5 * (oldguess + n/oldguess)
        oldguess = newguess
            
    return newguess

mySqrt(55, 5)

Exercise 17
#Write a function called fancySquare that will draw a square with fancy corners (spites on the corners). You should implement and use the drawSprite function from above. For an even more interesting look, how about adding small triangles to the ends of the sprite legs.
import turtle
ben = turtle.Turtle()
ben.color("SlateGray")
wn = turtle.Screen()
wn.bgcolor("LightSalmon ")

def drawSprite(t, some_number_legs, some_length_legs):
    t.shape("triangle")
    t.stamp()
    for i in range(some_number_legs):
        t.forward(some_length_legs)
        t.stamp()
        t.penup()
        t.backward(some_length_legs)
        t.pendown()
        t.left(360/some_number_legs)
        t.pendown()
        
def drawFancySquare(t, l, ll, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        drawSprite(t, l, ll)
        t.left(90)
        t.forward(sz)

drawFancySquare(ben, 5, 25, 30)

