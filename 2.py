import random

n = int(input('n = '))
if n != 2 and n != 3:
    print('n строго 2 или 3')
else:
    A = [[random.randint(-100, 100) for j in range(n)] for i in range(n)]
    print(A)

if n == 2:
    print(f'det A = {A[0][0] * A[1][1] - A[0][1] * A[1][0]}')
if n == 3:
    print(f'det A = {A[0][0]*A[1][1]*A[2][2] + A[2][0]*A[0][1]*A[1][2] + A[1][0]*A[0][2]*A[2][1] - A[2][0]*A[1][1]*A[0][2] - A[1][0]*A[0][1]*A[2][2] - A[0][0]*A[1][2]*A[2][1]}')

