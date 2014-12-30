Exercise 1
#What is the result of each of the following:
#a)‘Python’[1] --> y
#b)“Strings are sequences of characters.”[5] --> g
#c)len(“wonderful”) --> 9
#d)‘Mystery’[:4] --> Myst
#e)‘p’ in ‘Pineapple’ --> True
#f)‘apple’ in ‘Pineapple’ --> True
#g)‘pear’ not in ‘Pineapple’ --> True
#h)‘apple’ > ‘pineapple’ --> True
#i)‘pineapple’ < ‘Peach’ --> False

Exercise 2
#In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop tries to output these names in order.
prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p == "Q" or p == "O":
        print(p + "u" + suffix)
    else:
        print(p + suffix)
        
Exercise 3
#Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text - perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
#Write a function that counts the number of alphabetic characters (a through z, or A through Z) in your text and then keeps track of how many are the letter ‘e’. Your function should print an analysis of the text like this:
#Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.
ascii_lower='abcdefghijklmnopqrstuvwxyz'
proustPassage = """The places we have known do not belong solely to the world of space in which we situate them for our greater convenience. They were only a thin slice among contiguous impressions which formed our life at that time; the memory of a certain image is but regret for a certain moment; and houses, roads, avenues are as fleeting, alas, as the years."""
def countAlpha(passage):
    passage = passage.lower()
    alpha_counter = 0
    e_counter = 0
    for alpha in passage:
        if alpha in ascii_lower:
            alpha_counter += 1
            if alpha == 'e':
                e_counter +=1 
    print("Your text contains", alpha_counter, "alphabetic characters, of which", e_counter, ("(%d%%)" % round(e_counter/alpha_counter * 100)), "are 'e'.")

Exercise 4
#Print out a neatly formatted multiplication table, up to 12 x 12.
def multiTable(s):
    values = ["","","","","","","","","","","",""]
    for i in range(1, s + 1):
        values[0] = str(values[0]) + str(i) + "\t"
        values[1] = str(values[1]) + str(i * 2) + "\t"
        values[2] = str(values[2]) + str(i * 3) + "\t"
        values[3] = str(values[3]) + str(i * 4) + "\t"
        values[4] = str(values[4]) + str(i * 5) + "\t"
        values[5] = str(values[5]) + str(i * 6) + "\t"
        values[6] = str(values[6]) + str(i * 7) + "\t"
        values[7] = str(values[7]) + str(i * 8) + "\t"
        values[8] = str(values[8]) + str(i * 9) + "\t"
        values[9] = str(values[9]) + str(i * 10) + "\t"
        values[10] = str(values[10]) + str(i * 11) + "\t"
        values[11] = str(values[11]) + str(i * 12) + "\t"
    for i in values:
        print str(i) + "\n"

Exercise 5
#Write a function that will return the number of digits in an integer.
def integerCount(n):
    n = str(n)
    return len(n) 

Exercise 6
#Write a function that reverses its string argument.
def reverse(astring):
    newString = ""
    for char in astring:
        newString = char + newString
    return newString    

Exercise 7
#Write a function that mirrors its argument.
def mirror(mystr):
    mirror = ""
    for char in mystr:
        mirror = char + 
    return mystr + mirror

Exercise 8
Write a function that removes all occurrences of a given letter from a string.
def remove_letter(theLetter, theString):
    stripped = theString.replace(theLetter, "")
    return stripped

Exercise 9
#Write a function that recognizes palindromes.
def reverse(astring):
    newString = ""
    for char in astring:
        newString = char + newString
    return newString

def is_palindrome(myStr):
    if reverse(myStr) == myStr:
        return True
    return False

Exercise 10 
#Write a function that counts how many times a substring occurs in a string.
def count(sub, string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub):
            count += 1
    return count

Exercise 11
#Write a function that removes the first occurrence of a string from another string.
def remove(substr,theStr):
    if substr not in theStr:
        return theStr
    start = theStr.find(substr)
    length = len(substr)
    end = start + (length)
    return theStr[:start] + theStr[end:]

Exercise 12
Write a function that removes all occurrences of a string from another string
def remove_all(substr,theStr):
    newStr = theStr.split(substr)
    newStr = ''.join(newStr)
    return str(newStr)

Exercise 13
#Here is another interesting L-System called a Hilbert curve. Use 90 degrees:
#L
#L -> +RF-LFL-FR+
#R -> -LF+RFR+FL-
import turtle

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'L':
        newstr = '+RF-LFL-FR+'   # Rule 1
    elif ch == 'R':
        newstr = '-LF+RFR+FL-'
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(4, "L")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 90, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()

Exercises 14 - 17 are near duplicates of 13, but with switched out rules.

Exercise 20
#Write a function called removeDups that takes a string and creates a new string by only adding those characters that are not already present. In other words, there will never be a duplicate letter added to the new string.
def removeDups(astring):
    length = len(astring)
    comp = ""
    for i in astring:
        if i not in comp:
            comp = comp + i
    return comp

