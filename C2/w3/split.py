import re
print(re.split(r"[.?!]", "One Sentence. Another one. And the final one?"))
print(re.split(r"([.?!])", "One Sentence. Another one. And the final one?"))

#sub replaces the matched string
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Recievd an email for mani@sibi.com"))

#USE sub to replace second and first name
# /2 - means result[2]

print(re.sub(r"([\w\. ]*), ([\w\. ]*)", r"\2 \1", "Ladie, Ance"))


print(re.split(r"the|a", "One sentence. Another one? And the last one!"))