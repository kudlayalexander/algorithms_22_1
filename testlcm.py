import unittest

from main import lcm
from gcd_gen import GcdGenerator


class TestGcd(unittest.TestCase):
    def test_first_none(self):
        self.assertRaises(Exception, lcm, None, 1)

    def test_second_none(self):
        self.assertRaises(Exception, lcm, 1, None)

    def test_primes(self):
        self.assertEqual(lcm(7, 3), 21)

    def test_simple(self):
        self.assertEqual(lcm(6, 8), 24)

    def test_simple_long(self):
        self.assertEqual(lcm(1005002, 1354), 680386354)

    def test_random(self):
        gcd_gen = GcdGenerator()
        for i in range(10):
            gcd_gen.generate_values()
            self.assertEqual(lcm(gcd_gen.a_value, gcd_gen.b_value),
                             gcd_gen.lcm_value)


if __name__ == '__main__':
    unittest.main()
