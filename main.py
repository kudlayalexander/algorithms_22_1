import time
from typing import Any
import copy


def fibonacci_rec(num: int) -> int:
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)


def fibonacci_iter(num: int) -> int:
    n = 0
    n_next = 1
    fib = 0
    if num == 1:
        return 0
    if num == 2:
        return 1
    for i in range(num - 2):
        fib = n + n_next
        n = n_next
        n_next = fib
    return fib


def determinant(matrix: [[int]]):
    dlin = len(matrix[0])
    d = 0
    for i in range(len(matrix)):
        d += 1
        for j in range(len(matrix[i])):
            if dlin != len(matrix[i]):
                raise Exception("Матрица не квадратная")
    if d != dlin:
        raise Exception("Матрица не квадратная")

    if dlin == 1:
        return matrix[0][0]
    if dlin == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    def minor_matrix(Matr, i, j):
        copy_matr = copy.deepcopy(Matr)
        del copy_matr[i]
        for i in range(len(Matr[0]) - 1):
            del copy_matr[i][j]
        return copy_matr

    def det(Matr):
        m = len(Matr)
        n = len(Matr[0])
        if m != n:
            return None
        if n == 1:
            return Matr[0][0]
        x = 1
        determinant = 0
        for j in range(n):
            determinant += Matr[0][j] * x * det(minor_matrix(Matr, 0, j))
            x *= -1
        return determinant
    return det(matrix)


'''def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')'''


def main():
    for num in [3, 4, 5, 40]:
        # print_exec_time(lambda x: print(x, fibonacci_iter(x)), x=num)
        print(fibonacci_iter(num))

    matrix = [[3, -3, -5, 8],
                  [-3, 2, 4, -6],
                  [2, -5, -7],
                  [-4, 3, 5, -6]]
    print(f'determinant: {determinant(matrix)}')
    # print(fibonacci_iter(8))


if __name__ == '__main__':
    main()
