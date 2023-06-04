import re

#wild character and Character classes
print(re.search(r"[Pp]ython", "python"))
print(re.search(r"[a-z]id", "since i was a kid, i used to play football"))

print(re.search(r'id:[a-z]', 'id:nitro67'))

print(re.search(r'cloud[a-zA-Z0-9]', 'cloudy'))
print(re.search(r'cloud[a-zA-Z0-9]', 'cloud99'))

# Fill in the code to check if the text passed contains punctuation symbols:
# commas, periods, colons, semicolons, question marks, and exclamation points.

def check_punctuation (text):
  result = re.search(r"[,.:;!?]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

#search for any charcater which is not a letter
# for that use [^]
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces"))#this will match spaces
#we can add spaces to square bracket to avoid them

#use pipe symbol to match either one of options
print(re.search(r"cat|dog", "this is for cat"))
print(re.search(r"cat|dog", "this is for DOG", re.IGNORECASE))

print(re.search(r"cat|dog", "i like both cats and dogs"))#here we have 2 possible matches
#but we only get first match
#use re.findall to get all matches

print(re.findall(r"cat|dog", "this is for cat and my sweet dog"))

print(re.findall(r"id:[a-zA-Z0-9]", "id:nitro32"))
