import unittest
from anagram_checker import is_anagram

class MojeTesty(unittest.TestCase):

    def test_anagram_true(self):
        anagramy = (("abcd", "cbda"), ("abcd", "C da B"), ("I am Lord Voldemort", "Tom Marvolo Riddle"), ("jelenovipivonelej", "jELENOVI PIVo nelej"), ("skdjfh", "dj Fk sh"))

        for slova in anagramy:
            a = slova[0]
            b = slova[1]
            self.assertTrue(is_anagram(a, b))

    def test_anagram_false(self):
        anagramy = (("5", "1"), ("2", "3"), ("jk", "KL"), ("I am Lord Voldemort", "Tom Marvolo Riddler"))

        for slova in anagramy:
            a = slova[0]
            b = slova[1]
            self.assertFalse(is_anagram(a, b))