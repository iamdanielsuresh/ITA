# name = "daniel"
# roll_num = "nce20cs042"

# print("Name is {} and Roll Number is {}".format(name,roll_num))

# print("Name is {name1},rollnum is {rno}".format(name1="dani", rno=44))

price = 7.5
with_tax = price * 1.09 #9 %
print(price, with_tax)

#formated version using 2decimal places

print("Base price: Rs.{:.2f}. With Tax: Rs.{:.2f}".format(price, with_tax))

old = "what the fuck are u doing ajay ?"
new = old.replace("fuck", "fungus")
print(old)
print(new)