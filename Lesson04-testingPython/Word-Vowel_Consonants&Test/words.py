
"""
PART 1.
i.e. word examples
word1 = "functionality"
word2 = "apple"
word3 = "orange"

Create a class funtion that has the following functionality (as methods):

1. Takes a word as input
2. counts the vowels of a given word vowels: "aeiou"
3. counts the consonants of a given word "all the other letters that are not vowels"
4. Add tests using unittest

EXTRA:
Implement a way to read each word from  a text file.


PART 2.

Revist the code from yesterday for WordInfo (or use your own version)
Modify the code to do the following:

1. instead of reading one word, it reads a text file of words
2. implement a method called get_word_frequency() that counts the frequency of the words in the text
3. implement tests using pytest


"""

from string import ascii_letters


class words():
    """Calculator"""
    vowels = 'aeiou'

    def __init__(self, text):
        self.text = text.lower()
        with open(self.text) as f:
            text = f.readlines()
        self.text = ''.join(letter for letter in str(
            text) if letter in set(ascii_letters + ' ')).split(' ')

    def count_vowel(self):
        """
        get the number of vowels a word has
        """
        vowel_lst = [sum(1 for i in word if i in self.vowels)
                     for word in self.text]
        return dict(zip(self.text, vowel_lst))

    def count_consonants(self):
        """
        get the number of consonants a word has
        """
        consonants_lst = [sum(1 for i in word if i not in self.vowels)
                          for word in self.text]
        return dict(zip(self.text, consonants_lst))


if __name__ == '__main__':
    wd = words('text1.txt')
    print(wd.count_vowel())
    print(wd.count_consonants())
