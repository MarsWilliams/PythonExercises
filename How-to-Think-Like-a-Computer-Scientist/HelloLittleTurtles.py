Exercise 1
#Write a program that prints We like Python's turtles! 1000 times.
#Creates a loop for printing a message to the user
for x in range(1000):
    print("We like Python's turtles!")

Exercise 2
#Give three attributes of your cellphone object. Give three methods of your cellphone.
#Gives three attributes
cellphone_color = "peach"
cellphone_brand = "iPhone"
cellphone_ringtone = '''Young Magic's "Ocean"'''
#Gives three methods with related parameters
cellphone.ring(3)
cellphone.call("Benjamin")
cellphone.open(google)

Exercise 3
#Write a program that uses a for loop to print
#One of the months of the year is January
#One of the months of the year is February
#One of the months of the year is March
#etc ...
#Adds the months of the year to an array
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#Creates a loop to iterate over the months array and print a message to the user
for i in months:
    print("One of the months of the year is", i)
    
Exercise 4
#Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
#Write a loop that prints each of the numbers on a new line.
#Write a loop that prints each number and its square on a new line.
#Adds the numbers to an array called numbers
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#Creates a loop to print each of the numbers in the array to a new line
for i in numbers:
    print(i)
#Creates a loop to print each of the numbers in the array, and its square, to a new line    
for i in numbers:
    print(i, i*i)
    
Exercise 5
#Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
#An equilateral triangle
#A square
#A hexagon (six sides)
#An octagon (eight sides)
#imports turtle
import turtle
#sets variable wn to turtle.Screen
wn = turtle.Screen()

#Creates turtle called maggie
maggie = turtle.Turtle()
#Creates for loop so that maggie draws an equilateral triangle
for i in range(3):
    maggie.forward(100)
    maggie.right(360/3)

#tells the program to exit on click
wn.exitonclick()
    
#Creates turtle called abby
abby = turtle.Turtle()
#Creates for loop so that abby draws a square
for i in range(4):
    abby.forward(150)
    abby.right(360/4)

#tells the program to exit on click
wn.exitonclick()

#Creates turtle called andrew
andrew = turtle.Turtle()
#Creates for loop so that andrew draws a hexagon
for i in range(6):
    andrew.forward(25)
    andrew.left(360/6)

#tells the program to exit on click
wn.exitonclick()

#Creates turtle called shane
shane = turtle.Turtle()
#Creates for loop so that shane draws an octagon
for i in range(8):
    shane.forward(50)
    shane.left(360/8)

#tells the program to exit on click
wn.exitonclick() 

Exercise 6
#Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of a regular polygon. The program should draw the polygon and then fill it in.

#imports turtle
import turtle

#sets background screen
wn = turtle.Screen()

#defines fletch as turtle
fletch = turtle.Turtle()

#gives attributes to fletch
fletch.color(line_color)
fletch.fillcolor(fill_color)

#requests user input for side number, length, line color, and fill color
number_of_sides = int(input("How many sides?"))
length_of_side = int(input("What is the length of the side?"))
line_color = input("What is the line color?")
fill_color = input("What is the fill color?")

#tells fletch to fill the shape
fletch.begin_fill()

#creates a shape drawing loop with user-defined parameters
for i in range(number_of_sides):
    fletch.forward(length_of_side)
    fletch.left(360/number_of_sides)

#tells fletch to end shape fill
fletch.end_fill()

#tells the program to exit on click
wn.exitonclick()

Exercise 7
#A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading.
#imports turtle
import turtle
#sets background
wn = turtle.Screen
#defines turtle
drunk_pirate = turtle.Turtle()
#creates an array filled with the experimental data record of drunk pirate's turn angles
experimental_data = [160, -43, 270, -97, -43, 200, -940, 17, -87]
#creates a loop to iterate through the experimental_data array 
for i in experimental_data:
    drunk_pirate.left(i)
    drunk_pirate.forward(100)
    drunk_pirate_heading = drunk_pirate.heading()

#prints a message to the user that displays the drunk pirate's heading
print("The drunk pirate is now at heading", drunk_pirate_heading)

Exercise 9
#write a program to draw a pentagram
#imports turtle
import turtle
#sets background
wn = turtle.Screen()
#assigns turtle
alex = turtle.Turtle()

#creates loop to iterate through sides of star drawing
for i in range(5):
    alex.forward(100)
    alex.right(144)

#draws a circle around the star
alex.penup()
alex.left(72)
alex.circle(-50)

Exercise 10
#Write a program to draw a face of a clock with tick marks indicating each hour, and a turtle stamp in place of the number
#imports turtle
import turtle
#sets background
wn = turtle.Screen()
#assigns turtle
becca = turtle.Turtle()
#gives turtle attributes
becca.fillcolor("blue")
becca.shape("turtle")

#stamps turtle shape
becca.stamp()

#creates loop to iterate through 12 points, moving around in a circular formation
for i in range(12):
    becca.penup()
    becca.right(360/12)
    becca.forward(100)
    becca.pendown()
    becca.forward(5)
    becca.penup()
    becca.forward(15)
    becca.stamp()
    becca.penup()
    becca.backward(120)

Exercise 12
#Create a turtle and assign it to a variable. When you print its type, what do you get?
#imports turtle
import turtle
#assigns turtle to mabel
mabel = turtle.Turtle()
#prints the type of variable mabel
print(type(mabel))
#output reads <class 'Turtle'>

Exercise 13
#A sprite is a simple spider shaped thing with n legs coming out from a center point. The angle between each leg is 360/n degrees.
#Write a program to draw a sprite where the number of legs is provided by the user.

#sets up turtle
import turtle
wn = turtle.Screen()
sprite = turtle.Turtle()

#requests input from user for number of sprite legs
sprite_legs = int(input("How many legs does the sprite have?"))

#creates a loop to iterate through sprite legs, drawing out a leg, and adding a foot
for legs in range(sprite_legs):
    sprite.forward(100)
    sprite.circle(5)
    sprite.circle(-5)
    sprite.backward(100)
    sprite.left(360/sprite_legs)

#adds the body
sprite.dot(25)
