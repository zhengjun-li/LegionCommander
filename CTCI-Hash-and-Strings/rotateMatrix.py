"""
Rotate a nxn matrix 90 degrees to the right (in-place)
- n can be odd or even, if odd, the center element won't move
- saves top layer to a temp array, then rotate left to top, and so forth until we replace right with the tmep
    - then moves 1 layer deeper and repeats, using min_index and max_index to to bound ranges to represent inner layers
O(n^2) runtime - proof in onenote
O(n) space - to hold temp var
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
            matrix[max_index - i + min_index][layer] = matrix[max_index][max_index - i + min_index] #bottom to left
            matrix[max_index][max_index - i + min_index] = matrix[i][max_index] #right to bottom
            matrix[i][max_index] = temp #top to right
    return matrix

input = [[1, 2, 3, 4, 0], [5, 6, 7, 8, 0], [-1, -1, -1, -1, -1], [9, 10, 11, 12, 0], [13, 14, 15, 16, 0]]
result = rotate_matrix(input)
print(result)