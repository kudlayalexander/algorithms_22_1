import time
from typing import Any


# def fibonacci_rec(num: int) -> int:
#     """Returns the fibonacci number according to the number specified in the
#     parameter. Recursive implementation.
#
#     :param num: the ordinal number of the fibonacci number
#     :return: a fibonacci number
#     """
#     pass
#
#
# def fibonacci_iter(num: int) -> int:
#     """Returns the fibonacci number according to the number specified in the
#     parameter. Iterative implementation.
#
#     :param num: the ordinal number of the fibonacci number
#     :return: a fibonacci number
#     """
#     pass
#
#
# def determinant(matrix: [[int]]) -> int:
#     """Calculates the value of the matrix determinant
#     :param matrix: an integer matrix
#     :raise Exception: when the parameter value is not a square matrix
#     :return: the value of the matrix determinant
#     """
#     pass

# Рекурсивная реализация
def fibonacci_rec(num: int) -> int:
    if num<1:
        return Exception
    if num == 1:
        return 0
    if num == 2:
        return 1
    if num > 2:
        return fibonacci_rec(num-1) + fibonacci_rec(num-2)
# Итерационная реализация
def fibonacci_iter(num: int) -> int:
    if num == 1:
        return 0
    if num == 2:
        return 1
    fib = 0;
    fib2 = 1;
    for i in range (num-2):
        fib2 = fib2 + fib
        fib = fib2 - fib
    return fib2
# Определитель матрицы
def determinant(matrix: [[int]]) -> int:
    if len(matrix) == 0:
        return Exception
    if len(matrix) == 1:
        return matrix[0][0]
    sizes = list(set([len(i) for i in matrix]))
    if len(sizes)>1:
        raise Exception
    size = len(matrix)
    if size == 2: return x2(matrix) # если матрица 2х2
    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(size))
# возвращает определитель квадратной матрицы 2х2
def x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
# минор
def minor(matrix, i, j):
    matr = [row for t, row in enumerate(matrix) if t != i]
    matr = [col for t, col in enumerate(zip(*matr)) if t != j]
    return matr


def print_exec_time(func: callable(object), **kwargs) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def main():
    for num in [10, 20, 30, 35]:
        print_exec_time(lambda x: print(x, fibonacci_rec(x)), x=num)

    matrix = [[1, 2],
              [3, 4]]
    print(f'determinant: {determinant(matrix)}')


if __name__ == '__main__':
    main()
