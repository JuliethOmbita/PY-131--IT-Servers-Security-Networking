import unittest
from words import words


# the class is the "test suite"
class TestCalculatorMethods(unittest.TestCase):

    def setUp(self):
        self.wrd = words()

    def test_count_vowels_consonants(self):
        resp = self.wrd.count_vowels_consonants(['Algeria', 1894])
        alg_vowels = resp['Algeria']['vowels']
        self.assertEqual(alg_vowels, 4, "Algeria has 4 vowels")


if __name__ == '__main__':
    unittest.main()
