def get_matrix():
    n = int(input('Кол-во строк: '))
    m = int(input('Кол-во столбцов: '))
    matrix = [[0 for j in range(m)] for i in range(n)] 
    for i in range(n):
        for j in range(m):
            matrix[i][j] = float(input(f'matrix[{i}][{j}] = '))
            
    return matrix, n, m


def multiplication_of_element(matrix_a, matrix_b, i, j, n):
    element = 0
    for counter in range(n):
        element += matrix_a[i][counter] * matrix_b[counter][j]
    return element


def determinant(matrix_):
    matrix_size = matrix_[1]
    matrix = matrix_[0]

    print(matrix_)
    if (matrix_size != 2 and matrix_size != 3) or matrix_[1] != matrix_[2]:
        return None
    
    if matrix_size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return matrix[0][0]*matrix[1][1]*matrix[2][2] + matrix[2][0]*matrix[0][1]*matrix[1][2] + matrixA[1][0]*matrix[0][2]*matrix[2][1] - matrix[2][0]*matrix[1][1]*matrix[0][2] - matrix[1][0]*matrix[0][1]*matrix[2][2] - matrix[0][0]*matrix[1][2]*matrix[2][1]


def addition():
    matrix_a = get_matrix()
    matrix_b = get_matrix()
    
    if matrix_a[1] != matrix_b[1] or matrix_a[2] != matrix_b[2]:
        return 'Матрицы разного порядка'
    
    n = matrix_a[1]
    m = matrix_a[2]
    result = [[0 for j in range(m)] for i in range(n)] 
    for i in range(n):
        for j in range(m):
            result[i][j] = matrix_a[0][i][j] + matrix_b[0][i][j]

    return result


def subtraction():
    matrix_a = get_matrix()
    matrix_b = get_matrix()
    
    if matrix_a[1] != matrix_b[1] or matrix_a[2] != matrix_b[2]:
        return 'Матрицы разного порядка'
    
    n = matrix_a[1]
    m = matrix_a[2]
    result = [[0 for j in range(m)] for i in range(n)] 
    for i in range(n):
        for j in range(m):
            result[i][j] = matrix_a[0][i][j] - matrix_b[0][i][j]

    return result


def multiplication_matrix_and_number(matrix=None, coefficient=None):
    if matrix == None and coefficient == None:
        matrix = get_matrix()
        coefficient = float(input('Коэффициент = '))
    
    n = matrix[1]
    m = matrix[2]
    result = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = matrix[0][i][j] * coefficient

    return result
    


def multiplication_matrixes():
    matrix_a = get_matrix()
    matrix_b = get_matrix()

    if matrix_a[2] != matrix_b[1] and matrix_a[1] != matrix_b[2]:
        return "Невозможно умножить матрицы"
    elif matrix_a[2] == matrix_b[1]:
        n = matrix_a[1]
        m = matrix_b[2]
    else:
        n = matrix_a[2]
        m = matrix_b[1]

    result = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = multiplication_of_element(matrix_a[0], matrix_b[0], i, j, matrix_a[2])

    return result


def transposition(matrix=None):
    if matrix == None:
        matrix = get_matrix()
    
    n = matrix[1]
    m = matrix[2]
    result = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = matrix[0][j][i]

    return result


def invert_matrix():
    matrix = get_matrix()
    determinator_ = determinant(matrix)
    if determinator_:
        return 'Размерность не равна двум или трём или матрица не квадратная'

    matrix_transposited = (transposition(matrix), matrix[2], matrix[1])
    result = multiplication_matrix_and_number(matrix_transposited, determinator_)
    
    return result  
    

def main():
    navigation = {'1': addition, '2': subtraction, '3': multiplication_matrix_and_number, '4': multiplication_matrixes, '5': transposition, '6': invert_matrix}
    print("""Выберите действие:
1) Сложение
2) Вычитание
3) Умножение матрицы с числом
4) Умножение матриц
5) Транспонирование матрицы
6) Получение обратной матрицы // в процессе
""")
    return navigation[input('№: ')]()


if __name__ == '__main__':
    print(main())
