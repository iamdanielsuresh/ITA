def matrix(intial_num, end_of_first_row):
    n1 = intial_num
    n2 = end_of_first_row+1
    
    #create coloums
    for column in range(n1, n2):
    
        #create rows
        for row in range(n1, n2):

               print(column*row, end=" ")

        print()
            

matrix(1, 4)            
