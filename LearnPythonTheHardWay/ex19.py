#takes two arguments and prints them back within strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

#prints a string
print "We can just give the function numbers directly:"
#passes two arguments to the function cheese_and_crackers
cheese_and_crackers(20, 30)

#prints a string
print "Or, we can use variable from our script:"
#assigns an integer to a variable
amount_of_cheese = 10
#assigns an integer to a variable
amount_of_crackers = 50

#passes two arguments (that point to the information stored in two variables) to the function cheese_and_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prints a string
print "We can even do math inside too:"
#passes to equations to evaluate as arguments to the function cheese_and_crackers
cheese_and_crackers(10 + 20, 5 + 6)

#prints a string
print "And we can combine the two, variable and math:"
#passes two arguments to the function cheese_and_crackers. Both point to previously defined variables, and both modify the information contained in those variables.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
