import random


class GcdGenerator:
    """A class for generating three numbers from multiplication of primes,
    raised to a random power. The multipliers from gcd_value contains in a_value
    and b_value, but the other multipliers in the a_value and b_value does not
    intersect.
    The class is used for unit testing of the gcd function.

    Properties:
    -----------
    gcd_value -> int:
        Returns the greatest common divisor of a_value and b_value
    a_value -> int:
        Returns the number obtained as a result of multiplying primes
        raised to a random power. The number has both the same and different
        multipliers with b_value
    b_value -> int:
        Returns the number obtained as a result of multiplying primes
        raised to a random power. The number has both the same and different
        multipliers with a_value
    max_factor_cnt -> int:
        Returns the number of primes for the generated values
    Methods:
    -------
    generate_values(factor_cnt: int = 3, max_pow: int = 5) -> None:
        Generates new values of a, b and gcd.
        :param factor_cnt: the number of primes for the generated values, must
        be less or equal than max_factor_cnt property. The default value is 5.
        :param max_pow: the max bound for the random pow.
        The default value is 5.
        :return: None
    """
    def __init__(self):
        self.__primes: list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        self.__values: list[int] = [1, 1, 1]
        self.generate_values()

    @property
    def gcd_value(self) -> int:
        """Returns the greatest common divisor of a_value and b_value"""
        return self.__values[0]

    @property
    def a_value(self) -> int:
        """Returns the number obtained as a result of multiplying primes
        raised to a random power. The number has both the same and different
        multipliers with b_value"""
        return self.__values[1] * self.gcd_value

    @property
    def b_value(self) -> int:
        """Returns the number obtained as a result of multiplying primes
        raised to a random power. The number has both the same and different
        multipliers with a_value"""
        return self.__values[2] * self.gcd_value

    @property
    def max_factor_cnt(self) -> int:
        """Returns the number of primes for the generated values"""
        return len(self.__primes)

    def generate_values(self, factor_cnt: int = 5, max_pow: int = 5) -> None:
        """Generates new values of a, b and gcd.

        :param factor_cnt: the number of primes for the generated values, must
        be less or equal than max_factor_cnt property. The default value is 5.
        :param max_pow: the max bound for the random pow.
        The default value is 5.
        :return: None
        """
        if factor_cnt > len(self.__primes):
            factor_cnt = len(self.__primes)
        self.__values = [1, 1, 1]
        for prime in self.__primes[:factor_cnt]:
            rand_value_idx = random.randint(0, 2)
            rand_pow = random.randint(0, max_pow)
            self.__values[rand_value_idx] *= prime ** rand_pow
