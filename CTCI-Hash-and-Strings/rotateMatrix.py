"""
Compress given string "aaabbbbcc" into "a3b4c2", return original str if compressed is not shorter
- lowercase a-z only
"""
def rotate_matrix(matrix):
    n = len(matrix)
    layer_max = n // 2
    for layer in range(layer_max):
        min_index = layer #these allow you retreive each layer's sides in the matrix
        max_index = n - layer - 1
        for i in range(min_index, max_index):
            temp = matrix[layer][i] #save top of the matrix
            matrix[layer][i] = matrix[max_index - i + min_index][layer] #left to top
            matrix[max_index - i + min_index][layer] = matrix[max_index][max_index - i] #bottom to left
            matrix[max_index][max_index - i] = matrix[i][max_index] #right to bottom
            matrix[i][max_index] = temp #top to right
    return matrix

input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
result = rotate_matrix(input)
print(result)