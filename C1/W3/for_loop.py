values = [23,52,59,37,48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum : " + str(sum) + " - Average:" + str(sum/length))

product = 1
for n in range(1,10):
    product *= n 

print(product)