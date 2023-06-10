#simple matching

import re

result = re.search(r"aza","plaza")
  #r infront of string indicates raw strings
#always use raw string for python
print(result)

result2 = re.search(r"sibi","sibinism")
print(result2)

not_match = re.search(r"mani", "goutham")
print(not_match)

# ^ means circumflence
# it indicates the staring of a line
# $ indicates end of the line

print(re.search(r"^mani", "manikandan"))
print(re.search(r"sibi$", "ashvinsibi"))

# . can match any character
print(re.search(r".gay", "i am gay"))

print(re.search(r"hello", "HELLOworld"))#o/p will be none
#to remove case sensitivity
#use re.IGNORECASE

print(re.search(r"hello", "HELLOworld", re.IGNORECASE))


# Fill in the code to check if the text passed contains the vowels a, e and i,
# with exactly one occurrence of any other character in between.
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

