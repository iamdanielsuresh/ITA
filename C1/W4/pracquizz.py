# def pig_latin(text):
#   say = ""
#   # Separate the text into words
#   words = text.split()
#   for word in words:
#     # Create the pig latin word and add it to the list
#     new_word += word[1:] + word[0] + "ay"
#     # Turn the list back into a phrase
#   return new_word
		
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"




def group_list(group, users):
  members = ""
  for member in users:
    members = group + " : " + ", ".join(users)

  
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"