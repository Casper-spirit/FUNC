

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix1 = []
        for j in range(m):                           #  ПРАВИЛЬНОЕ РЕШЕНИЕ ПО УСЛОВИЮ В ДЗ
            matrix1.append(value)
        matrix.append(matrix1)
    return matrix
mat = get_matrix(3, 4, 5)
print(mat)

