def get_matrix (n, m, value):
    matrix = []
    for row in range (n):
        matrix.append([])
        for column in range (m):
            matrix[row].append(value)
    return matrix

n = int(input("Введите количество строк "))
m = int(input("Введите количество столбцов "))
value = int(input("Введите значение "))
result = get_matrix(n, m, value)
print(result)



