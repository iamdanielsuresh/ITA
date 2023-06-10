#finding repeated charachters using .*
import re

print(re.search(r"Py.n", "Pygamlion"))
#now including *
print(re.search(r"Py.*n", "Pygamlion"))
print(re.search(r"Py.*n", "Python Programming"))


#using + to combine
print(re.search(r"o+l+", "wolly"))
print(re.search(r"o+l+", "oily skin"))

# ? indicates optional character
print(re.findall(r"p?each", "for each person, 3 peaches"))

#Escaping Characters
#suppose we want to match special charcters
#we have to use /
print(re.search(r".com", "welcome"))#not using /
#using /
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "www.mydomain.com"))

# \w* is used to detect all alpha numeric charc
print(re.search(r"\w*", "welcome_home_boy"))
# \d for matching digits
# \s for matching whitespace charcters
# Fill in the code to check if the text passed has at least 2 groups 
# of alphanumeric characters
# (including letters, numbers, and underscores) 
# separated by one or more whitespace characters.

def check_character_groups(text):
  result = re.search(r"\w+\s\w+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False





