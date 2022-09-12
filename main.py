from gcd_gen import *
def gcd_recursive(a: int, b: int) -> int:
    """Calculates the greatest common divisor of two numbers.
    Recursive implementation.

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if a is None or b is None:
        raise Exception("a or b is None!")
    if a == 0:
        return b
    return gcd_recursive(b % a, a)


def gcd_iterative_slow(a: int, b: int) -> int:
    """Calculates the greatest common divisor of two numbers.
    Iterative implementation using subtraction.

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if a is None or b is None:
        raise Exception("a or b is None!")
    while a != 0 and b != 0:
        if a >= b:
            a -= b
        else:
            b -= a
    return max(a,b)


def gcd_iterative_fast(a: int, b: int) -> int:
    """Calculates the greatest common divisor of two numbers
    Iterative implementation using division.

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if a is None or b is None:
        raise Exception("a or b is None!")
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return max(a,b)


def lcm(a: int, b: int) -> int:
    """Calculates the least common multiple of two numbers

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: the least common multiple
    """
    return int(a * b / gcd_iterative_fast(a, b))


def main():
    print(lcm(2,2))


if __name__ == '__main__':
    main()
