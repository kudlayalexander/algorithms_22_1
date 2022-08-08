import time

from fibonacci.fibbonacci import fibonacci


def print_fibonacci(num: int) -> None:
    print("%d: %d".format(num, fibonacci(num)))


def get_exec_time(function: callable(object), argument: int) -> float:
    start_time = time.time()
    function(argument)
    return time.time() - start_time


def main():
    for num in [10, 20]:
        print("duration: %s seconds".format(get_exec_time(fibonacci, num)))


if __name__ == '__main__':
    main()
