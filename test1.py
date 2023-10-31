import unittest

def freq(s):
    d={}
    s=s.lower()
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

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

  

class TestFreq(unittest.TestCase):
    def testIsFreq(self):
        sentence = "malayalam"
        self.assertTrue(freq(sentence))
   
    def testNullInput(self):
        ret = freq("")
        self.assertFalse(ret)


if __name__ == "__main__":
    unittest.main()


