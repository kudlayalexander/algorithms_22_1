import unittest

from main import generate_permutations


class TestPermutation(unittest.TestCase):
    def test_none(self):
        self.assertRaises(Exception, generate_permutations, None, [])

    def test_empty(self):
        self.assertCountEqual(generate_permutations(frozenset()), [])

    def test_single_num(self):
        self.assertCountEqual(generate_permutations(frozenset((1,))), ['1'])

    def test_double_num(self):
        self.assertCountEqual(generate_permutations(frozenset((1, 2))),
                              ['12', '21'])

    def test_double_bool(self):
        self.assertCountEqual(generate_permutations(frozenset((True, False))),
                              ['TrueFalse', 'FalseTrue'])

    def test_triple_num(self):
        self.assertCountEqual(generate_permutations(frozenset((1, 2, 3))),
                              ['123', '132', '213', '231', '312', '321'])

    def test_triple_char(self):
        self.assertCountEqual(generate_permutations(frozenset(('a', 'b', 'c'))),
                              ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_quadruple_num(self):
        self.assertCountEqual(generate_permutations(frozenset((1, 2, 3, 4))),
                              ['1234', '1243', '1324', '1342', '1423', '1432',
                               '2134', '2143', '2314', '2341', '2413', '2431',
                               '3124', '3142', '3214', '3241', '3412', '3421',
                               '4123', '4132', '4213', '4231', '4312', '4321'])


if __name__ == '__main__':
    unittest.main()
