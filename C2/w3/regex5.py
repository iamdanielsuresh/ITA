import re
#print countries whoes name start with A and ends with a
print(re.search(r"A.*a","Argentina"))
print(re.search(r"A.*a", "Azhakabinjan"))#this result is not correct
print(re.search(r"^A.*a$", "Azhakabinjan"))

#python variable rule
pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"
print(re.search(pattern,"_this_is_a_valid_variable_name"))
print(re.search(pattern,"1his is not"))

# code to check if the text passed looks like a standard sentence,
# meaning that it starts with an uppercase letter, 
# followed by at least some lowercase letters 
# or a space, and ends with a period, question mark, or exclamation point.

# def check_sentence(text):
#     result = re.search(r"^[A-Z][A-Za-z0-9 ]*[.?!]*$", text)
#     return result != None
# print(check_sentence("i said get out!"))
# print(check_sentence("It was very good!!"))



def is_valid_web_address(text):
  pattern = r"^[a-zA-Z0-9_-]+\.[a-zA-Z]{2,}$"
  pattern2 = r"^\S+\.\w+$"
  result = re.match(pattern2, text)
  return result is not None

print(is_valid_web_address("gmail.com")) # True
print(is_valid_web_address("www@google")) # False
print(is_valid_web_address("www.Coursera.org")) # True
print(is_valid_web_address("web-address.com/homepage")) # False
print(is_valid_web_address("My_Favorite-Blog.US")) # True
