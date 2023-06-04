# animals = ["lion", "zebra", "Dolphin", "Monkey"]
# chars = 0
# for animal in animals:
#     chars += len(animal)

# print("Total characters : {}, Avg Len : {}".format(chars, chars/len(animals)))  

# #using enumerate function
# The first value of the tuple is the index and the second value is the element itself.




# for index , name in enumerate(animals):
#     print("{} - {}".format(index + 1, name))


# Complete the skip_elements function to return every 
# other element from the list, this time 
# using the enumerate function to check
# if an element is in an even position or an odd position.

def skip_elements(elements):
	# code goes here
	result = []
	for index, element in enumerate(elements):
		if (index + 1)%2 != 0:
			result.append("{}".format(element))
	return result
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) 
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) 