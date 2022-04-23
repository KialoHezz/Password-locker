import unittest
from user_class import user 
from credential_class import credential


class Test_user(unittest.TestCase):
    '''
    Arqument of unittest.testCase which help us to test case
    function to setUp : user account before they are test
    '''
    def setUp(self ):
        self.new_user =  user("hezzykialo", "ngoma123")

    def test_init(self):
        '''
        function test if the object are initialized properly
        '''
        self.assertEqual(self.new_user.username,"hezzykialo")
        self.assertEqual(self.new_user.password,"ngoma123")

    '''
    to test if the user is saved properly in user_list
    '''
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(user.user_list),1)


class TestCredential(unittest.TestCase):
    '''
    '''