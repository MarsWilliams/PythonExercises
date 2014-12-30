Exercise 1
#Draw a reference diagram for a and b before and after the third line of the following python code is executed:
a = [1, 2, 3]
b = a[:] #making a copy of a, b now points to that copy
b[0] = 5 #reassigning the zeroth index of b to the integer 5
         #b now points to the list [5, 2, 3]
         #a still points to [1, 2, 3]

Exercise 2
#Create a list called myList with the following six items: 76, 92.3, “hello”, True, 4, 76. Do it with both append and with concatenation, one item at a time.
myList = []
myList.append(76)
myList.append(92.3)
myList.append("hello")
myList.append(True)
myList = myList + [4]
myList = myList + [76]

Exercise 3
#Starting with the list in Exercise 1, write Python statements to do the following:
#Append “apple” and 76 to the list.
#Insert the value “cat” at position 3.
#Insert the value 99 at the start of the list.
#Find the index of “hello”.
#Count the number of 76s in the list.
#Remove the first occurrence of 76 from the list.
#Remove True from the list using pop and index.
myList = [76, 92.3, 'hello', True, 4, 76]
myList.append("apple")
myList.append(76)
myList.insert(3, "cat")
myList.insert(0,99)
myList.index("hello")
myList.count(76)
myList.remove(76)
myList.pop(myList.index(True))

Exercise 4
#Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random module). Write a function called average that will take the list as a parameter and return the average.
import random
listLength = 100
list = []
for i in range(listLength):
    q = random.randrange(0,1000)
    list.append(q)

def average(list):
    return sum(list)/listLength

Exercise 
#Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)
import random
listLength = 5
list = []
for i in range(listLength):
    q = random.randrange(0,1000)
    list.append(q)
print list

def maximum(list):
    list.sort()
    return list.pop()
    
    #or, if you wanted to keep the list unaltered
    
import random
listLength = 5
list = []
for i in range(listLength):
    q = random.randrange(0,1000)
    list.append(q)
print list

def maximum(list):
    list.sort()
    return list.[-1]

Exercise 6:
#Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
def sum_of_squares(xs):
    squares = 0
    for i in xs:
         squares = squares + i**2
    return squares
    
Exercise 7
#Write a function to count how many odd numbers are in a list.
def odd(list):
    count = 0
    for i in list:
        if i%2 != 0:
            count += 1
    return count

Exercise 8
#Sum up all the even numbers in a list.
def even(list):
    even = []
    for i in list:
        if i%2 == 0:
            even.append(i)
    return sum(even)

Exercise 9
#Sum up all the negative numbers in a list.
def odd(list):
    odd = []
    for i in list:
        if i%2 != 0:
            odd.append(i)
    return sum(odd)

Exercise 10
#Count how many words in a list have length 5.
def five(list):
    five = 0
    for i in list:
        if len(i) == 5:
            five += 1
    return five

Exercise 11
#Sum all the elements in a list up to but not including the first even number.
def someOdds(list):
    someOdds = []
    for i in list:
        if i%2 == 0:
            return sum(someOdds)
        someOdds.append(i)

Exercise 12
#Count how many words occur in a list up to and including the first occurrence of the word “sam”.
def sam(list):
    count = 0
    for i in list:
        if i == "sam":
            return count
        count += 1
    return count
    return sum(someOdds)

Exercise 13
#Although Python provides us with many list methods, it is good practice and very instructive to think about how they are implemented. Implement a Python function that works like the following:
#a)count
#b)in
#c)reverse
#d)index
#e)insert

def counting(list):
    count = 0
    for i in list:
        count += 1
    return count

def inIt(list, item):
    for i in list:
        if i == item:
            return True
    return False

def reverso(list):
    tsil = []
    for i in list:
        tsil = [i] + tsil
    return tsil

def indexer(list, item):
    index = 0
    for i in list:
        if i == item:
            return index
        index += 1

def inserter(list, position, item):
    return list[:position+1] + [item] + list[position:]

Exercise 14
#Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:
def replace(s, old, new):
    s = s.split(old)
    s = new.join(s)
    print s
    return s
