# #example of dominos

# for left in range(7):
#     for right in range(left, 7):
#         print("[" +str(left) + "|" + str(right) +"]", end="")
#     print()   

# #team pairings

# teams = ['Barca', 'Real Madrid', 'ManCity', 'ManU', 'Bayern']   
# print("The possible fixtures are : ")

# for home_team in teams:
#     for away_team in teams:
#         if home_team != away_team:
            
#             print("[" +str(home_team) + " vs " + str(away_team) +" ] ", end ="")
#             print()

# using function inside for loop

def greetings(name):
    for greet in name:
        print("Hello " +str(greet))
greetings(['daniel','sibi', 'mani', 'vasanth'])             

# for x in range(2):
#     print("This is the outer loop iternation num " + str(x))
#     for y in range(2):
#         print("Inner loop iternation numbwe " +str(y))
#     print("Exit inner loop")   
