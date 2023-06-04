import os
# os.remove("novel.txt")
# os.rename("novel1.txt", "new-novel.txt")
# print(os.path.exists("new-novel.txt"))
# print(os.path.exists("novel.txt"))
if os.path.exists("novel.txt") == True :
    
    with open("novel.txt", "r") as file:
        print(file.read())

        with open("novel.txt", "a") as file:
            file.write("I had this wired dream")
        file = open("novel.txt")
        print(file.read())
    os.rename("novel.txt", "novel_new.txt")    
else:
    print("The file you provided does not exist")

        
    

