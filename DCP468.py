def rotate_matrix_slow(matrix):
    n = len(matrix)
    new_matrix = [[None for _ in range(n)] for _ in range(n)]

    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            new_matrix[c][n - r - 1] = val

    return new_matrix

def rotate_matrix_fast(matrix):
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            p1 = matrix[i][j]
            p2 = matrix[j][n-i-1]
            p3 = matrix[n-i-1][n-j-1]
            p4 = matrix[n-j-1][i]

            matrix[j][n-i-1] = p1
            matrix[n-i-1][n-j-1] = p2
            matrix[n-j-1][i] = p3
            matrix[i][j] = p4

    return matrix
mtrx = [[1,2,3], [4,5,6], [7,8,9]]
print("Slow rotate")
print(rotate_matrix_slow(mtrx))
print("Fast rotate")
print(rotate_matrix_fast(mtrx))