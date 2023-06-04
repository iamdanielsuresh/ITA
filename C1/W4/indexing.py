# #access any letter 

# variable1 = "This is a example string"
# print(variable1[0])
# #select multiple char
# print(variable1[:5])#from 0 - 4
# print(variable1[4:])
# #access from back
# print(variable1[-5:])

#how to get a certain character num 

# pets = " Cats and Dogs"
# print(pets.index("a"))
# print(pets.index("Cats"))

#a company recently switched to a new domain , but some of the email
#address are still using old domain, 
#write a program to replace old with new domain

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
