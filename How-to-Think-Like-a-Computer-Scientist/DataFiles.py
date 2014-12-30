#Exercise 1
#The following sample file called studentdata.txt contains one line for each student in an imaginary class. The student’s name is the first thing on each line, followed by some exam scores. The number of scores might be different for each student.
#joe 10 15 20 30 40
#bill 23 16 19 22
#sue 8 22 17 14 32 17 24 21 2 9 11 17
#grace 12 28 21 45 26 10
#john 14 32 25 16 89
#Using the text file studentdata.txt write a program that prints out the names of students that have more than six quiz scores.

infile = open("studentdata.txt", "r")

aline = infile.readline() #could omit this line if using a for loop

while aline:
    data = aline.split()
    if len(data[1:]) > 6:
        print data[0]
    aline = infile.readline() #could omit this line if using a for loop

infile.close()

#Exercise 2
#Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the average grade for each student, and print out the student’s name along with their average grade.

infile = open("studentdata.txt", "r")

aline = infile.readline()

while aline:
    aline = (aline.rstrip()).split()
    scores = 0
    for a in aline[1:]:
        scores = scores + int(a)
    print "%s's average score is %s." % (aline[0].capitalize(), str(int(scores / len(aline[1:]))))
    aline = infile.readline()

infile.close()

#Exercise 3
#Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the minimum and maximum score for each student. Print out their name as well.

infile = open("studentdata.txt", "r")

aline = infile.readline()

while aline:
    aline = (aline.rstrip()).split()
    print "%s's maximum score is %s and h/er minimum score is %s." % (aline[0].capitalize(), max(aline[1:]), min(aline[1:])) 
    aline = infile.readline()

infile.close()

#At the bottom of this page is a very long file called mystery.txt The lines of this file contain either the word UP or DOWN or a pair of numbers. UP and DOWN are instructions for a turtle to lift up or put down its tail. The pairs of numbers are some x,y coordinates. Write a program that reads the file mystery.txt and uses the turtle to draw the picture described by the commands and the set of points.

infile = open("mystery.txt", "r")

aline = infile.readline()
import turtle
wn = turtle.Screen()
ben = turtle.Turtle()
while aline:
    aline = (aline.rstrip()).split()
    if aline[0] == "UP":
        ben.penup()
    elif aline[0] == "DOWN":
        ben.pendown()
    else:
        ben.goto(int(aline[0]), int(aline[1]))
    aline = infile.readline()

infile.close()
