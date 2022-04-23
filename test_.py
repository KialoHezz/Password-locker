import unittest
from user_class import user

class Test_user(unittest.TestCase):
    '''
    Arqument of unittest.testCase which help us to test case
    function to setUp : user account before they are test
    '''
    def setUp(self):
        self.new_user =  user("hezzykialo", "ngoma123")

    def test_init(self):
        '''
        function test if the object are initialized properly
        '''
        self.assertEqual(self.new_user.username,"hezzykialo")
        self.assertEqual(self.new_user.password,"ngoma123")

    