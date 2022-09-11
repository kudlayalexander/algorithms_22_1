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

    prev_prev_number = 0
    prev_number = 1

    if num == 1:
        return prev_prev_number
    if num == 2:
        return prev_number
    for i in range(2, num):
        prev_number = prev_prev_number + prev_number
        prev_prev_number = prev_number - prev_prev_number
    return prev_number


def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """

    check_matrix_param = __check_matrix__(matrix)

    if check_matrix_param == -1:
        raise Exception("Matrix is not defined or contains no elements")
    elif check_matrix_param == 0:
        raise Exception("Matrix is not square")
    elif check_matrix_param == 1:
        return matrix[0][0]
    elif check_matrix_param == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    param_list = []
    minor_list = []
    current_index_col = 0
    index_zero = __search_zero_row__(matrix)

    for i in range(len(matrix)):
        index_minor = 0
        minor = [[] * (len(matrix) - 1) for _ in range(len(matrix) - 1)]
        for row in range(len(matrix)):
            if row == index_zero:
                continue
            for col in range(len(matrix[row])):
                if col == current_index_col:
                    continue
                minor[index_minor].append(matrix[row][col])
            if index_minor < len(matrix) - 2:
                index_minor += 1
        current_index_col += 1
        minor_list.append(minor)

    current_index_col = 0
    for i in matrix[index_zero]:
        current_index_col += 1
        power = (index_zero + 1) + current_index_col
        number = i * pow(-1, power)
        param_list.append(number)

    y = 0
    for i in range(len(param_list)):
        y += param_list[i] * determinant(minor_list[i])

    return y


def __check_matrix__(matrix: [[int]]) -> int:
    """Checks the shape of the matrix
    :param matrix: an integer matrix
    :return: -1 - if the matrix is not defined or contains no elements;
    0 - if the matrix is not square;
    1 - if the matrix is 1x1;
    2 - if the matrix is 2x2;
    3 - if the matrix is 3x3...;
    """

    if not matrix:
        return -1

    count_row = 0
    count_col = 0

    for row in range(len(matrix)):
        count_row += 1
        for col in range(len(matrix[row])):
            count_col += 1

    if count_row == (count_col / count_row):
        return count_row

    return 0


def __search_zero_row__(matrix: [[int]]) -> int:
    """Finds the string index with more zeros
    :param matrix: an integer matrix
    :return: index value if there are zeros or 0 if there are no zeros
    """

    index_row = 0
    zero_counter_all = 0

    current_index_row = 0
    zero_counter_row = 0

    for row in range(len(matrix)):
        for col in matrix[row]:
            if col == 0:
                zero_counter_row += 1
        if zero_counter_all < zero_counter_row:
            zero_counter_all = zero_counter_row
            index_row = current_index_row
        current_index_row += 1

    return index_row

# Падает ошибка TypeError: 'type' object is not subscriptable
# Не получилось разобраться, как фиксануть((

# def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
#     start_time = time.time()
#     func(**kwargs)
#     print(f'duration: {time.time() - start_time} seconds')


def main():
    # for num in [10, 20, 30, 35]:
    #    print_exec_time(lambda x: print(x, fibonacci_iter(x)), x=num)

    matrix = [[1, 2, 3, 5, 5],
              [3, 4, 0, 1, 1],
              [1, 1, 1, 3, 4],
              [0, 1, 0, 1, 0],
              [5, 6, 1, 8, 2]]
    print(f'determinant: {determinant(matrix)}')


if __name__ == '__main__':
    main()
