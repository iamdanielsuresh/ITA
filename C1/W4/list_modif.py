fruits = ["Pineapple", "Banana"]
fruits.append("Kiwi") #this method will add element to end of list
print(fruits)

fruits.insert(0,"Orange")#adds to the specified position
print(fruits)

#remove element

fruits.remove("Banana")
print(fruits)

#remove with index

fruits.pop(2)
print(fruits)

fruits[1] = "Strawberry"
print(fruits)