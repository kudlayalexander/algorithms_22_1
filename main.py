import copy
import time
from typing import Any


def fibonacci_rec(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Recursive implementation.
    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num == 0:
        return 1
    if num == 1:
        return 0
    return fibonacci_rec(num - 2) + fibonacci_rec(num - 1)


def fibonacci_iter(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.
    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num == 1:
        return 0
    if num == 2 or num == 3:
        return 1
    fib1 = fib2 = 1
    for i in range(3, num):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    l = len(matrix)
    for i in range(l):
        if len(matrix[i]) != l:
            raise Exception("Матрица не квадратная")
    if l == 1:
        return matrix[0][0]
    if l == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # Определяем строку с наибольшим кол-вом нулей
    most_nulls_count = 0
    most_nulls_row = 0
    current_row = 0
    for row in matrix:
        null_count = 0
        for number in row:
            if number == 0:
                null_count += 1
        if null_count > most_nulls_count:
            most_nulls_row = current_row
        current_row += 1
    sum = 0
    for i in range(l):
        matrix_copy = copy.deepcopy(matrix)
        for j in range(l):
            for k in range(l):
                matrix_copy[most_nulls_row][k] = None
                matrix_copy[j][i] = None
        for j in range(l):
            matrix_copy[j] = [x for x in matrix_copy[j] if x is not None]
        new_matrix = []
        for j in range(l):
            if len(matrix_copy[j]) != 0:
                new_matrix.append(matrix_copy[j])
        sum += matrix[most_nulls_row][i] * determinant(new_matrix) * ((-1) ** (i + most_nulls_row))
    return sum


def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
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
