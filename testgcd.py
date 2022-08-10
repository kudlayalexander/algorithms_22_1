import unittest
import random

from main import gcd


class TestGcd(unittest.TestCase):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    def test_first_none(self):
        self.assertRaises(Exception, gcd, None, 1)

    def test_second_none(self):
        self.assertRaises(Exception, gcd, 1, None)

    def test_simple(self):
        self.assertEqual(gcd(9, 3), 3)

    def test_simple_long(self):
        self.assertEqual(gcd(1005002, 1354), 2)

    def test_random(self):
        for i in range(10):
            values = self.__generate_random_values()
            self.assertEqual(gcd(values["a"], values["b"]), values["gcd"])

    def __generate_random_values(self):
        values = [1, 1, 1]
        for prime in self.primes:
            values[random.randint(0, 2)] *= prime ** random.randint(0, 5)
        return {"gcd": values[0], "a": values[0] * values[1],
                "b": values[0] * values[2]}


if __name__ == '__main__':
    unittest.main()
