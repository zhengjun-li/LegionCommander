"""
If an element is 0, set its column and row to 0 as well (in-place)
-
O(nm) time
"""
def zero_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    #which rows/columns are to be zero'd out
    # I chose to use sets because of O(1) access time, although modifying is O(n),
    # we will be accessing much more than modifying. 
    zero_columns = set()
    zero_rows = set()
    for i in range(n): #O(n*m)
        for j in range(m):
            #O(1) for all set lookup/insert operations (unless weird collisions)
            if matrix[i][j] == 0: 
                if i not in zero_rows:
                    zero_rows.add(i)
                if j not in zero_columns:
                    zero_columns.add(j)
    
    #zero out the rows/columns
    for i in range(n): #O(n*m)
        if i in zero_rows:
            matrix[i] = [0]*n
        else:
            for j in range(m):
                if j in zero_columns:
                    matrix[i][j] = 0
        
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

input = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 0, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 0, 25]]
result = zero_matrix(input)
print_matrix(result)