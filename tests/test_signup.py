import unittest
from Banking_With_Python.user import User

class TestSignup(unittest.TestCase) :
    def setUp(self):
        self.user_info = ("rahaf","ahmad","12345678")
        return super().setUp()
    
if __name__ == "__main__":
    unittest.main()
