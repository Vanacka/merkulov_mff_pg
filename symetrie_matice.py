def symetricka_hl_diagonala(matrix, n) -> int:
    for i in range(n - 1):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return 0
    return 1


def symetricka_ved_diagonala(matrix, n) -> int:
    for i in range(n - 1):
        for j in range(n - i - 2, -1, -1):
            if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
                return 0
    return 1


def symetricka_prostredni_osa(matrix, n) -> int:
    for i in range(n // 2):
        for j in range(n):
            if matrix[j][i] != matrix[j][n - i - 1]:
                return 0
    return 1


vstup = input().split()
matrix = [vstup]

for i in range(len(vstup) - 1):
    matrix.append(input().split())

n = len(matrix[0])

print(symetricka_hl_diagonala(matrix, n), symetricka_ved_diagonala(matrix, n), symetricka_prostredni_osa(matrix, n))
