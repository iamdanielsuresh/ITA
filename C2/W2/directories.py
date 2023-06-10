import os
print(os.getcwd())
# os.mkdir("new_dir")
# os.chdir("new_dir")
# print(os.getcwd())

# os.rmdir("new_dir")
print(os.listdir("Intern"))
print()
dir = "Intern"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
