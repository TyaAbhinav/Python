"""
test_formater.py
By: Abhinav Tyagi
Date: 02NOV22
"""

import unittest, formater

class TestFormater(unittest.TestCase):
    def test_lower(self):
        test_text = "ABHINAV"
        result = formater.convert_lower(test_text)
        self.assertEqual(result, "abhinav")
    
    def test_upper(self):
        test_text = "Abhinav"
        result = formater.convert_upper(test_text)
        self.assertEqual(result, "ABHINAV")

if __name__ =="__main":
    unittest.main()