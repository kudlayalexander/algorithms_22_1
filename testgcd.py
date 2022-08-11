import unittest

from main import gcd
from gcd_gen import GcdGenerator


class TestGcd(unittest.TestCase):
    def test_first_none(self):
        self.assertRaises(Exception, gcd, None, 1)

    def test_second_none(self):
        self.assertRaises(Exception, gcd, 1, None)

    def test_simple(self):
        self.assertEqual(gcd(9, 3), 3)

    def test_simple_long(self):
        self.assertEqual(gcd(1005002, 1354), 2)

    def test_random(self):
        gcd_gen = GcdGenerator()
        for i in range(10):
            gcd_gen.generate_values()
            self.assertEqual(gcd(gcd_gen.a_value, gcd_gen.b_value),
                             gcd_gen.gcd_value)


if __name__ == '__main__':
    unittest.main()
