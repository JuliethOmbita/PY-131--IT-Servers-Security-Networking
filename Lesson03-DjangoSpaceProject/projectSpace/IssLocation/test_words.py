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

        # self.wrd.add(3,3)
        # self.assertDictEqual(self.wrd.count_vowels_consonants[['Algeria', 1894]], {'Algeria': {'vowels': 4, 'consonants': 3, 'message': ''}, 1894: {
        #  'vowels': 0, 'consonants': 0, 'message': 'impout invalid'}}, "tests addition of two arguments on integers")


if __name__ == '__main__':
    unittest.main()
