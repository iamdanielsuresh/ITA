# def odd_or_even(number):
#     a = "The number is even"
#     b = "The number is odd"
#     if number % 2 == 0 :
#         print(a)
    
    
#     return False
# c = int(input("num : "))
# odd_or_even(c)

def username_valid(username):
    if len(username) < 3:
        print("The username entred is invalid,too short")
    elif len(username) > 10:
        print( "invalid, reduce ur character number")

    elif type(username) != str:
        print("u cant add numbers")
    else :
        print("Valid username")       
username_valid("daniel")       