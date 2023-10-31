import unittest

def palindrome(s):
    if type(s)==str:
        return s==s[::-1]
    else:
        return False

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

if __name__ == "__main__":
    unittest.main()


