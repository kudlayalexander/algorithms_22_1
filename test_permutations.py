import unittest

from main import get_permutations


class TestPermutation(unittest.TestCase):
    def test_none(self):
        self.assertRaises(Exception, get_permutations, None)

    def test_0(self):
        self.assertCountEqual(get_permutations(0), [])

    def test_1(self):
        self.assertCountEqual(get_permutations(1), ['1'])

    def test_2(self):
        self.assertCountEqual(get_permutations(2), ['12', '21'])

    def test_3(self):
        result = ['123', '132', '213', '231', '312', '321']
        self.assertCountEqual(get_permutations(3), result)


if __name__ == '__main__':
    unittest.main()
