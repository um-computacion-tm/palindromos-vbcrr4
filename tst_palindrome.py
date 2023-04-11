import unittest
from pali import palindrome

class TestPalindrome (unittest.TestCase):
    def test_1(self):
        result = palindrome('neuquen')
        self.assertEqual (result, True)
    def test_2(self):
        result = palindrome('reconocer')
        self.assertEqual (result, True)
    def test_3(self):
        result = palindrome('orejero')
        self.assertEqual (result, True)
    def test_4(self):
        result = palindrome('Ojo')
        self.assertEqual (result, True)
    def test_5(self):
        result = palindrome('perro')
        self.assertEqual (result, False)
    def test_6(self):
        result = palindrome("araña")
        self.assertEqual (result,False)


    

if __name__ == '__main__':
    unittest.main()