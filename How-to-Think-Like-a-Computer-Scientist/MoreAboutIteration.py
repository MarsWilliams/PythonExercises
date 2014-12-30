Exercise 1
#Add a print statement to Newton’s sqrt function that prints out better each time it is calculated. Call your modified function with 25 as an argument and record the results.
def sqrt(n):
    oldguess = 0.5 * n
    better = 0.5 * (oldguess + n/oldguess)
    while True:
        print better
        better = 0.5 * (oldguess + n/oldguess)
        if oldguess == better:
            return False
        oldguess = better

sqrt(25)

Exercise 3
#Write a function, is_prime, that takes a single integer argument and returns True when the argument is a prime number and False otherwise.
def is_prime(n):
    divcount = 0
    for i in range(1, n+1):
        if n % i == 0:
            divcount += 1
    if divcount == 2:
        return True
    return False

Exercise 4
#Modify the walking turtle program so that rather than a 90 degree left or right turn the angle of the turn is determined randomly at each step.
import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(random.random()*365)
    else:
        t.right(random.random()*365)

    t.forward(50)

wn.exitonclick()
