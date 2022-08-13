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

    def test_4(self):
        result = ['1234', '1243', '1324', '1342', '1423', '1432', '2134',
                  '2143', '2314', '2341', '2413', '2431', '3124', '3142',
                  '3214', '3241', '3412', '3421', '4123', '4132', '4213',
                  '4231', '4312', '4321']
        self.assertCountEqual(get_permutations(4), result)


if __name__ == '__main__':
    unittest.main()
