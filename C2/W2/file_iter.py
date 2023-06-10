# with open("Python/ITA/C2/W2/spider.txt") as file:
#     for line in file:
#         print(line.upper())


# with open("Python/ITA/C2/W2/spider.txt") as file2:
#     for line in file2:
#         print(line.strip().upper())      


#method 2 : using list and sort()
file = open("Python/ITA/C2/W2/spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)


