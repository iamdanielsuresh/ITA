
import re
#capturing groups
#using group methord
# result = re.search(r"^(\w*), (\w*)$", "Suresh, Daniel")
# print(result.groups())
# print(result[0])
# print(result[1])
# print(result[2])
# print("{} {}".format(result[2],result[1]))

def rearrene_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    print(result)
    print(result[0])
    print(result[1])
    print(result[2])
    if result is None:
        return name
    return "{} {}".format(result[2],result[1])
print(rearrene_name("Suresh, Daniel"))
print(rearrene_name("Girish, Anusree"))
print(rearrene_name("K. C, Sreeraj"))
    
    
    