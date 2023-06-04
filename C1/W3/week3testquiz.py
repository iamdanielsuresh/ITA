# def count_by_10(end):
#     count =""
#     for number in range(0,end+100,10):
#         count += str(number) + " "
#     return count.strip()
# print(count_by_10(100))
 #0 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190   


#use nested loops to create matrix


# def matrix(initial_number, end_of_first_row):
#     n1 = initial_number 
#     n2 = end_of_first_row+1


#     for column in range(n1, n2):


#         for row in range(n1, n2):


#               print(column*row, end=" ")

#         print() 
# matrix(1, 4)


# start = 18
# while start >= 0:
#     print(start, end=" ")
    
#     start -= 3






# def X_figure(salary):
#     tally = 0

#     if salary == 0:
#         tally += 1
#     while salary >= 1:
#         salary = salary/10
#         tally += 1
#     return tally   
# print("The CEO has a " + str(X_figure(2300000)) + " figure salary.") 


# def count_fig(salary):
#     count = 0
#     salary =""
#     for x in salary:
#         count+=1
#     return count
# print("The CEO has a " + str(X_figure(2300000)) + " figure salary")





#  Skill 3: Using while loops with if-else statements
# Use a function to accept two variable integers. 

# Use nested if-else statements and while loops to 
# count up or count down from the first variable to the second variable.   
        
def elevator_floor(enter, exit):
    floor = enter
    elevator_direction = ""

    if enter > exit:
        elevator_direction = "Going down: "
        while floor >= exit:
            elevator_direction += str(floor)
            if floor > exit:
                elevator_direction += " -->  "
            floor -= 1
    else:
        elevator_direction = "Going up: "
        while floor <= exit:  
            elevator_direction += str(floor)
            if floor < exit:
                elevator_direction += "  -->  "
            floor += 1
    return elevator_direction

print(elevator_floor(1,4))
print()
print(elevator_floor(6,2))     
print(0)       




    

