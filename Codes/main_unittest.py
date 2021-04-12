import unittest
import unit_testing_unittest

class TestUnitTest(unittest.TestCase):

    def test_text(self):
        text = "Python"
        result = unit_testing_unittest.upper_text(text)
        self.assertEqual(result,"PYTHON")
        
    def test_mutiple_text(self):
        text = "monty python"
        result = unit_testing_unittest.upper_text(text)
        self.assertEqual(result,"MONTY PyTHON")
        
if __name__ == "__main__":
    unittest.main()
   