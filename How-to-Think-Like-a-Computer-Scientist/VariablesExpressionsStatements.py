Exercise 3
#Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off.
#asks a user for the time and converts the response to an integer
time_now_in_hours = int(input("What time is it now, in hours?"))
#asks the user for their desired amount of sleep
time_left_to_sleep_in_hours = int(input("For how many hours would you like to sleep) to sleep?"))
#prints the time they would need to wake up
print((time_now_in_hours+time_left_to_sleep_in_hours%24))

Exercise 4
#It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights. Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.
#asks a user for the day and converts the response to an integer
departure_day_of_the_week = int(input("On which day of the week would you like to leave?"))
#asks the user for their desired length of stay
length_of_stay = int(input("How many days would you like to stay?"))
#prints the day they would return
print(departure_day_of_the_week + length_of_stay % 7)

Exercise 5
#Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.
#splits a string and assigns each word in the string to a unique variable
a,b,c,d,e,f,g,h,i,j = "All work and no play makes Jack a dull boy".split(" ")
#concatenates the variables into a string
print(a, b, c, d, e, f, g, h, i, j)

Exercise 6
#Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.
print(6*(1-2))

Exercise 7
#The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
#Amount = Principal \cdot \left( 1 + \frac {rate}{periods} \right) ^ {time\; \cdot\; periods} (in LaTeX)
#Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.
#Assigns integers to variables
P = 10000
n = 12
r = 0.08
#asks the user for the amount of time that the interest will compound, and converts their response into an integer
t = int(input("For how many years will the money be compounded?"))
#prints a message to the user that displays the results of the compounded interest calculation, with the result displayed to the third decimal place. 
print("The final amount after",t,"years is",round((P*(1+(r/n))**(n*t)),2))

Exercise 8
#Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.
#loads math module
import math
#requests user input for circle radius
radius = int(input("What is the radius of your circle?"))
#calculation for area of circle, using a math function as a value
area = (radius * math.pi)**2
#prints a message to the user that displays the area of their circle
print("The area of your circle is", area, "!")

Exercise 9
#Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. Print a nice message with the answer.
#requests user input for rectangle width
width = int(input("What is the width of your rectangle?"))
#requests user input for rectangle height
length = int(input("What is the height of your rectangle?"))
#calculation for area of rectangle
area = width * length
#prints a message to the user that displays the area of their rectangle
print("The area of your rectangle is", area)

Exercise 10
#Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer.
#Requests user input for the number of miles driven
miles_driven = int(input("How many miles have you driven?"))
#Requests user input for the number of gallons used
gallons_used = int(input("How many gallons have you used on your journey?"))
#Calculates MPG
miles_per_gallon = miles_driven / gallons_used 
#Prints a message to the user that displays their car's miles per gallon rate on the journey
print("You car achieved", miles_per_gallon, "MPG on this journey.")

Exercise 11
#Write a program that will convert degrees celsius to degrees fahrenheit.
#Requests user input for degrees celsius
degrees_celsius = int(input("How many degrees celcius?"))
#Calculates degrees fahrenheit
degrees_fahrenheit = degrees_celsius * 1.8 + 32
#Prints a message to the user that displays the degrees fahrenheit
print("It is", degrees_fahrenheit, "degrees fahrenheit outside now.")

Exercise 12
#Write a program that will convert degrees fahrenheit to degrees celsius.
#Requests user input for degrees fahrenheit
degrees_fahrenheit = int(input("How many degrees fahrenheit?"))
#Calculates degrees celsius
degrees_celsius = ((degrees_fahrenheit - 32) * 5) / 9
#Prints a message to the user that displays the degrees celsius
print("It is", degrees_celsius, "degrees celsius outside now.")
