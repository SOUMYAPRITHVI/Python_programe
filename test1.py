import unittest
from task1 import panagram,palindrome,freq

class TestPanagram(unittest.TestCase):
    def testIsPanagram(self):
        sentence = "the quick brown fox jumps over the lazy dog"
        self.assertTrue(panagram(sentence))

    def testIsNotPanagram(self):
        sentence = "the quick brown fox jumped over the lazy dog"
        self.assertFalse(panagram(sentence))
    
    def testNullInput(self):
        ret = panagram("")
        self.assertFalse(ret)


class TestPalindrome(unittest.TestCase):
    def testIsPalindrome(self):
        sentence = "malayalam"
        self.assertTrue(palindrome(sentence))

    def testIsNotPalindrome(self):
        sentence = "English"
        self.assertFalse(palindrome(sentence))
    
    def testNullInput(self):
        ret = palindrome("")
        self.assertTrue(ret)

    def testNonstrInput(self):
        ret = palindrome(546.78)
        self.assertFalse(ret)

  

class TestFreq(unittest.TestCase):
    def testDict(self):
        s = "aabbc @?a"
        expected_dict={'a': 3,'b': 2,'c': 1,' ':1,'@': 1,'?': 1}
        self.assertDictEqual(expected_dict,freq(s))
   
    def testNullInput(self):
        ret = freq("")
        self.assertFalse(ret)


if __name__ == "__main__":
    unittest.main()


