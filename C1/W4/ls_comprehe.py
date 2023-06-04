#list comprehention is used to create a 
#list using range fun

#print a list with 10 multiples of 7
#normal way
multiples = []
for x in range(1, 11):
    multiples.append(x*7)
print(multiples)    

#using comprehention

multiples1 = [ x*7 for x in range(1,11)]
print(multiples1)

lang = ["English", "Malayalam", "Hindi", "Tamil"]
languages = [(x , name) for x, name in enumerate(lang)]
length = [len(y) for y in lang]
print(languages)
print(length)