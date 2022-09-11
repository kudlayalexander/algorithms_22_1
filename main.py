import time
from typing import Any


def fibonacci_rec(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Recursive implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)


def fibonacci_iter(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num == 1:
        return 0
    if num == 2:
        return 1
    prev = 1
    prevprev = 0
    for i in range(2, num):
        prev += prevprev
        prevprev = prev - prevprev
    return prev


def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    if not __matrix_check(matrix):
        raise Exception("when the parameter value is not a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    row = __best_row(matrix)
    result = __algebra(matrix, row)
    return result


def __matrix_check(matrix: [[int]]) -> bool:  # matrix order check
    if len(matrix) < 1:
        return False
    for row in range(len(matrix)):
        if len(matrix[row]) != len(matrix):
            return False
    return True


def __best_row(matrix: [[int]]) -> int:  # best matrix row (count of 0 in row)
    zero_count = 0
    max_zero_count = 0
    zero_row_number = 0
    for row in range(len(matrix)):
        zero_count = 0
        for col in range(len(matrix)):
            if matrix[row][col] == 0:
                zero_count += 1
            if zero_count > max_zero_count:
                max_zero_count = zero_count
                zero_row_number = row
    return zero_row_number


def __algebra(matrix: [[int]], row: int) -> int:  # result
    result = 0
    for i in range(len(matrix)):
        if not matrix[row][i] == 0:
            minor = [[]]  # Минор (двумерный массив)
            minor_row = 0  # Номер строки в двумерном массиве
            for j in range(len(matrix)):
                if not j == row:
                    buf_col = 0  # Номер столбца в двумерном массиве
                    buf_list = []  # Строки минора
                    for k in range(len(matrix)):
                        if not k == i:
                            buf_list.append(matrix[j][k])
                            buf_col += 1
                    minor.append(buf_list)
                    minor_row += 1
            minor.pop(0)  # Из-за append нулевой элемент это пустой массив [], он удаляется
            res_buf = matrix[row][i] * determinant(minor)  # Рекурсия
            if (row + i) % 2 == 1:
                res_buf *= -1
            result += res_buf
    return result


def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def main():
    for num in [10, 20, 30, 35]:
        print_exec_time(lambda x: print(x, fibonacci_iter(x)), x=num)
    # Изменил матрицу
    matrix = [[1, -2, 3],
              [-4, 5, -6],
              [7, -8, 9]]
    print(f'determinant: {determinant(matrix)}')


if __name__ == '__main__':
    main()
