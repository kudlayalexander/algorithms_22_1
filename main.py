import time
from functools import lru_cache
from typing import Any


# region Fibonacci


@lru_cache()
def fibonacci_rec(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Recursive implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num == 1:
        return 0
    elif num == 2:
        return 1
    return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)


def fibonacci_iter(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    first = 0
    second = 1

    for _ in range(num-1):
        second += first
        first = second - first
    return first
# endregion

# region Determinant


def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    if not right_matrix(matrix):
        raise Exception()
    if len(matrix) == 1:
        return matrix[0][0]
    max_row_count_zero = 0
    row_index = 0
    for index, row in enumerate(matrix):
        if max_row_count_zero < row.count(0):
            row_index = index
            max_row_count_zero = row.count(0)

    answer = 0
    for value_index in range(len(matrix)):
        if matrix[row_index][value_index] != 0:
            answer += pow(-1, (row_index + value_index+2)) * matrix[row_index][value_index] * \
                           minor_determinant(matrix, row_index, value_index)

    return answer


def minor_determinant(matrix: [[int]], row: int, column: int) -> int:
    """Calculates the value of the minor matrix determinant
    :param matrix: an integer matrix
    :param row: row that should be excluded from the matrix to create minor
    :param column: column that should be excluded from the matrix to create minor
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    len_matrix = len(matrix) - 1
    # A new matrix consisting of zeros
    new_matrix = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)]
    # Creating a new matrix by columns
    new_row, new_column = 0, -1
    for minor_value in range(len_matrix + 1):
        if minor_value != column:
            new_column += 1
            new_row = 0
            for minor_row in range(len_matrix + 1):
                if minor_row != row:
                    new_matrix[new_row][new_column] = matrix[minor_row][minor_value]
                    new_row += 1
    # recursion to find determinant of main matrix
    return determinant(new_matrix)


def right_matrix(matrix: [[int]]) -> bool:
    """Decides whether the matrix is in the correct form for calculating the determinant
    :param matrix: an integer matrix
    :return: True if it is in the correct form and false if it's not
    """
    row_counter = len(matrix)
    if row_counter == 0:
        return False
    for row in matrix:
        if len(row) != row_counter:
            return False
    return True
# endregion


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