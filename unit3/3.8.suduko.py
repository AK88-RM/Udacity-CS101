correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
              [2,3,1,4],
              [4,1,2,3],
              [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(list1):
    n = 0
    for row in list1:  # get n, length of square
        n = n + 1
    for row in list1:   
       temp_row = []      # empty temporary row at beginning
       for entry in row:
            if type(entry) != int:  # check for char & decimals
                return False
            if entry > n or entry < 1: # check for number outside range
                return False
            if entry in temp_row:  # check for repeated entry in row
                return False
            temp_row.append(entry) # add entry into temporary array

    row_with_column_data = []        # test for repeated data in column
    for j in range (0,n):
        for i in range (0,n):
            row_with_column_data.append(list1[i][j])  # populate the row
        temp_row = []
        for entry in row_with_column_data:
            if entry in temp_row:
                return False           # return False if repeated entry
            temp_row.append(entry)    # populate temp_row
        row_with_column_data = []   # zero out the column     
    return True



    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False
