animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals :
    chars += len(animals)

for index, animal in enumerate(animals):  
    print("{}  - {}".format(index + 1, animal))  

print("Total characters : {}, Average length : {}".format(chars, chars/len(animals)))

winners = ["Ash"]