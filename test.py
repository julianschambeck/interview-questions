import unittest
import random
from solutions import isunique, ispermut, URLify, ispalindrom_permut, one_away, squeeze_with_counts

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
        self.assertEqual('', URLify(''))

    def test_ispalindrom_permut(self):
        self.assertTrue(ispalindrom_permut("Tact Coa"))
        s = list("abcba")
        random.shuffle(s)
        s = ''.join(s)
        self.assertTrue(ispalindrom_permut(s))
        self.assertTrue(ispalindrom_permut(''))
        self.assertFalse(ispalindrom_permut("cdaabb"))
        self.assertFalse(ispalindrom_permut("cd"))

    def test_one_away(self):
        self.assertTrue(one_away("pale", "bale")) # replace
        self.assertTrue(one_away("pales", "pale")) # delete
        self.assertFalse(one_away("paless", "pale"))
        self.assertTrue(one_away("pale", "pales")) # insert
        self.assertTrue(one_away("pale", "pale")) # 0 edits is ok too
        self.assertFalse(one_away("pale", "bake")) # edits > 1 

    def test_squeeze_with_counts(self):
        self.assertEqual(squeeze_with_counts("aabbbbccccccd"), "a2b4c6d1")
        # expect original string because compressed one is longer here
        self.assertEqual(squeeze_with_counts("aabbc"), "aabbc")
        self.assertEqual(squeeze_with_counts("c"), "c")
        self.assertEqual(squeeze_with_counts(""), "")
        # some with capital letters
        self.assertEqual(squeeze_with_counts("BBBBbbbbCC"), "B4b4C2")
        self.assertEqual(squeeze_with_counts("BBBCCCd"), "B3C3d1")

if __name__ == "__main__":
    unittest.main()
