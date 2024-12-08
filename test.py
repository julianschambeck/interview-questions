import unittest
from solutions import isunique, ispermut, URLify

class TestSolutions(unittest.TestCase):
    def test_isunique(self):
        self.assertTrue(isunique("abcde"))
        self.assertFalse(isunique("aabcdee"))
        self.assertTrue(isunique(''))
        self.assertTrue(isunique('b'))

    def test_ispermut(self):
        self.assertTrue(ispermut("abc", "abc"))
        self.assertTrue(ispermut("abc", "cab"))
        self.assertFalse(ispermut("aabc", "abc"))
        self.assertFalse(ispermut("abc", ''))
        self.assertFalse(ispermut('', "abc"))
        self.assertFalse(ispermut("abc", 'bcac'))

    def test_URLify(self):
        s = "Mr. John Smith"
        self.assertEqual("Mr.%20John%20Smith", URLify(s))
        self.assertEqual("%20", URLify(" "))
        self.assertEqual("", URLify(""))

if __name__ == "__main__":
    unittest.main()
