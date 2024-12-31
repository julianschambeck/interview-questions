import unittest
import random
from solutions import isunique, ispermut, URLify, ispalindrom_permut, one_away, squeeze_with_counts, mat_rotate, mat_rotate_space, zero_mat, binary_search, ThreeStacks

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

    def test_mat_rotate(self):
        mat = [[0,0,0],
            [1,1,1],
            [0,1,0]]
        rot = [[0,1,0],
                [1,1,0],
                [0,1,0]]
        self.assertEqual(mat_rotate(mat), rot)
        self.assertEqual(mat_rotate([]), [])
        self.assertEqual(mat_rotate_space(mat), rot)
        self.assertEqual(mat_rotate_space([]), [])

    def test_zero_mat(self):
        m = [[0, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1]]
        other = [row[:-1] for row in m] # 4x3 matrix
        zeroed = [[0, 0, 0, 0],
                [0, 1, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

        self.assertEqual(zero_mat(m), zeroed)
        self.assertEqual(zero_mat(other), [row[:-1] for row in zeroed])

    def test_binary_search(self):
        nums = sorted([15, 10, 23, 50, 2, 1, 7])
        chars = sorted(['d', 'c', 'a', 'g', 'z'])

        self.assertTrue(binary_search(nums, 23))
        self.assertFalse(binary_search(nums, 80))
        self.assertTrue(binary_search(chars, 'z'))

    def test_three_stacks(self):
        stacks = ThreeStacks(3)
        stacks.push(0, 'a')
        stacks.push(0, 'b')
        stacks.push(0, 'c')

        stacks.push(1, 0)
        stacks.push(1, 1)
        stacks.push(1, 2)

        stacks.push(2, "some val")

        stacks.pop(0)
        stacks.pop(1)
        stacks.pop(1)
        stacks.pop(2)

if __name__ == "__main__":
    unittest.main()
