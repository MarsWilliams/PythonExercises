# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  newstr = ""
  for i in range(0, len(str), 2):
    newstr += str[i]
  return newstr


# Given a non-empty string like "Code" return a string like "CCoCodCode". 
def string_bits(str):
  newstr = ""
  for i in range(0, len(str), 2):
    newstr += str[i]
  return newstr


# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
  count = 0
  sub = str[-2:]
  for i in range(len(str)-2):
    if (str[i] + str[i+1] == sub):
      count += 1
  return count

 def array_front9(nums):
  newnum = nums[:4]
  nines = 0
  for i in range(len(newnum)):
    if newnum[i] == 9:
      return True
  else:
    return False
    