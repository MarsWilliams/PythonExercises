#Exercise 1
#Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored.

sentence = raw_input("Please enter a sentence:").lower().replace(" ", "")
letter_count = dict()
for letter in sentence:
    if letter.isalpha():
        if letter not in letter_count:
            letter_count[letter] = 1 
        letter_count[letter] = letter_count[letter] + 1
        
for key in sorted(letter_count):
    print "%s: %d" % (key, letter_count[key])

#Exercise 2
#Give the Python interpreter’s response to each of the following from a continuous interpreter session:

#>>> d = {'apples': 15, 'bananas': 35, 'grapes': 12}
#>>> d['banana'] would return error
#>>> d['oranges'] = 20 would add the key value pair 'oranges' : 20 to d
#>>> len(d) would return 4
#>>> 'grapes' in d would return True
#>>> d['pears'] would return error
#>>> d.get('pears', 0) would return 0
#>>> fruits = d.keys() would return 'apples', 'bananas', 'grapes', 'oranges'
#>>> fruits.sort() would return 'apples', 'bananas', 'grapes', 'oranges' 
#>>> print(fruits) would return 'apples', 'bananas', 'grapes', 'oranges'  
#>>> del d['apples'] would return {'bananas': 35, 'grapes': 12}
#>>> 'apples' in d would return error

#Exercise 3
#Write a program called alice_words.py that creates a text file named alice_words.txt containing an alphabetical listing of all the words, and the number of times each occurs, in the text version of Alice’s Adventures in Wonderland. (You can obtain a free plain text version of the book, along with many others, from http://www.gutenberg.org.) 
#How many times does the word, alice, occur in the book?

import string
import collections

infile = open("aliceinwonderland.txt", "r")
outfile = open("alice_words.txt", "w")

nonwords = string.punctuation + string.digits

word_count = dict()
                 
for aline in infile:    
    aline = aline.replace("'s", "").lower()
    for ch in nonwords:
        if ch in aline:
            aline = aline.replace(ch, " ")
    aline = aline.split()
    for word in aline:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1
               
for key in sorted(word_count):
    outfile.write("%s: %d\n" % (key, word_count[key]))

outfile.write("The word Alice appears %d times in the novel" % (word_count["alice"]))

infile.close()
outfile.close()

#Exercise 4
#What is the longest word in Alice in Wonderland? How many characters does it have?
import string
import collections

infile = open("aliceinwonderland.txt", "r")
outfile = open("alice_words.txt", "w")

nonwords = string.punctuation + string.digits

word_count = dict()
                 
for aline in infile:    
    aline = aline.replace("'s", "").lower()
    for ch in nonwords:
        if ch in aline:
            aline = aline.replace(ch, " ")
    aline = aline.split()
    for word in aline:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1

words = word_count.keys()

base = len(words[0])
word = ""

for i in words:
    word_length = len(i)
    if word_length > base:
        base = word_length
        word = str(i)
 
for key in sorted(word_count):
    outfile.write("%s: %d\n" % (key, word_count[key]))

outfile.write("The word Alice appears %d times in the novel. The longest word in the novel is %s, and it is %d characters long." % (word_count["alice"], word, base))

infile.close()
outfile.close()

#Exercise 5
#Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.

pirate_speak = {"sir": "matey", "hotel": "fleabag inn", "student": "swabbie", "boy": "matey", "madam": "proud beauty", "professor": "foul blaggart", "restaurant": "galley", "your": "yer", "excuse": "arr", "students": "swabbies", "are": "be", "lawyer": "foul blaggart", "the": "th'", "restroom": "head", "my": "me", "hello": "avast", "is": "be", "man": "matey"}
kings_speech = (raw_input("What say ye landlubber?")).lower().split()

piratized = ""

for word in kings_speech:
    if word in pirate_speak:
        word = pirate_speak[word]
        piratized = piratized + word + " "
    elif word not in pirate_speak:
        piratized = piratized + word + " "

print piratized.capitalize()
