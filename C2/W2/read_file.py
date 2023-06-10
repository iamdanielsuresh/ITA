file = open("Python/ITA/C2/W2/spider.txt")

print(file.readline())#read line by line
print(file.read())#read from current 

file.close()

with open("Python/ITA/C2/W2/spider.txt") as file:
    print(file.readline())
 #when opening using with, python automatically close
 # the opened file
 
 #file_iteration
 