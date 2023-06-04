import re
#suppose we wantletters of  exactly 5 words
print(re.search(r"\w{5}", "A ghost"))
print(re.findall(r"\w{5}", "A scary ghost"))
print(re.findall(r"\w{5}", "A scary ghost appeard")) #the output contain the word we dont want
#use \b in the begining and end
print(re.findall(r"\b\w{5}\b", "A scary ghost appeard"))

#limiting range
print(re.findall(r"\w{3,5}", "A scary ghost appeard of nowhere"))

