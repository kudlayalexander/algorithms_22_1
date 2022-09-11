import time
import copy
from typing import Any


def fibonacci_rec(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Recursive implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    # выход из рекурсии
    if num == 1:
        return 0
    # выход из рекурсии
    elif num == 2:
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
    elif num == 2:
        return 1
    prev, current = 1, 1
    for i in range(2, num):
        prev, current = current, prev + current
    return prev


def null_horizontal(matrix):
    max_horizontal_null = 0
    max_horizontal_index = 0
    for (horizontal_index, horizontal_vector) in enumerate(matrix):
        null_counter = horizontal_vector.count(0)
        if null_counter > max_horizontal_null:
            max_horizontal_index = horizontal_index
            max_horizontal_null = null_counter
    return [max_horizontal_null, max_horizontal_index]


def null_vertical(matrix):
    matrix_order = len(matrix)
    max_vertical_null = 0
    max_vertical_index = 0
    for vertical_index in range(matrix_order):
        null_counter = [horizontal[vertical_index] for horizontal in matrix].count(0)
        if null_counter > max_vertical_null:
            max_vertical_index = vertical_index
            max_vertical_null = null_counter
    return [max_vertical_null, max_vertical_index]


def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    matrix_order = len(matrix)
    answer = 0
    for horizontal_elements in matrix:
        if len(horizontal_elements) != matrix_order:
            raise Exception
    if matrix_order == 1:
        answer = matrix[0][0]
        return answer
    if matrix_order == 2:
        answer = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return answer
    else:
        horizontal_null_count, horizontal_null_index = null_horizontal(matrix)
        vertical_null_count, vertical_null_index = null_vertical(matrix)
        if horizontal_null_count > vertical_null_count:
            horizontal_vector = matrix[horizontal_null_index]
            for vertical_index in range(matrix_order):
                if horizontal_vector[vertical_index] != 0:
                    sign = (-1) ** (horizontal_null_index + 2 + vertical_index)
                    value = horizontal_vector[vertical_index]
                    new_matrix = []
                    for horizontal in range(matrix_order):
                        if horizontal != horizontal_null_index:
                            nw = []
                            for vertical in range(matrix_order):
                                if vertical != vertical_index:
                                    nw.append(matrix[horizontal][vertical])
                            new_matrix.append(copy.deepcopy(nw))
                            nw.clear()
                    answer += sign * value * determinant(new_matrix)
            return answer
        else:
            vertical_vector = [horizontal[vertical_null_index] for horizontal in matrix]
            for horizontal_index in range(matrix_order):
                if vertical_vector[horizontal_index] != 0:
                    sign = (-1) ** (vertical_null_index + 2 + horizontal_index)
                    value = vertical_vector[horizontal_index]
                    new_matrix = []
                    for horizontal in range(matrix_order):
                        if horizontal != horizontal_index:
                            nw = []
                            for vertical in range(matrix_order):
                                if vertical != vertical_null_index:
                                    nw.append(matrix[horizontal][vertical])
                            new_matrix.append(copy.deepcopy(nw))
                            nw.clear()
                    answer += sign * value * determinant(new_matrix)
            return answer


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
