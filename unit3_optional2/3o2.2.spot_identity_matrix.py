def is_identity_matrix(matrix):
    i = 0
    j = 0
    k = 0
    l = 0
    for element in matrix[0]:      
        k = k + 1
    for element in matrix:
        l = l + 1
    if l != k:
        return False        
    for i in range(0,len(matrix)):
        if matrix [i][i] != 1:
             return False
        for j in range (0,len(matrix)):
             if matrix[i][j] != 0:
                 if i == j:
                     continue
                 else:
                    return False
    
                
    return True

#        result = matrix[i][j] + matrix[j][i]

    if result == 0:
        return True
    else:
        return False



# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False           

           
