import unittest
from Banking_With_Python.user import User

class TestLogin(unittest.TestCase) :
    def test_login(self):
        user_info = ("29d51716-7ae7-4c59-bee3-ae561cf6124c","Rof$1234")
        self.assertEqual(user_info,[True,"29d51716-7ae7-4c59-bee3-ae561cf6124c"]) 

if __name__ == "__main__":
    unittest.main()
