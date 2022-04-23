import unittest
from user_class import user

class Test_user(unittest.TestCase):
    '''
    Arqument of unittest.testCase which help us to test case
    function to setUp : user account before they are test
    '''
    def setUp(self):
        self.new_user =  user("hezzykialo", "ngoma123")

    