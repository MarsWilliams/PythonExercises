Exercise 
#Use a for statement to print 10 random numbers.
#load Python module
import random
for i in range(10):
   print(random.random())


Exercise 2
#Repeat the above exercise but this time print 10 random numbers between 25 and 35.
#load Python module
import random
#create loop to iterate through 10 pseudo-random numbers
for i in range(10):
  print(random.randrange(25, 35))

Exercise 3
#The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle is related to the lengths of the other two sides. Look thru the math module and see if you can find a function that will compute this relationship for you. Once you find it, write a short program to try it out.
#import math
import math
#get user input for known side lengths
x = int(input("What is the length of one known side of your triangle?"))
y = int(input("What is the length of the other known side of your triangle?"))
hypotenuse_length = math.hypot(x, y)
print("The length of the hypotenuse of your triangle is", hypotenuse_length) 

Exercise 4
#import math and cmath modules
import math
import cmath
#print the result of both modules; note that they are the same value
print("The approximate value of pi is", math.pi)
print("The true value of pi is", cmath.pi)
