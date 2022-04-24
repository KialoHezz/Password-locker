import unittest
from user_class import user
from credetial_class import credential

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = user("hezron", "ngoma123")

    def test_init(self) :
        self.assertEqual(self.new_user.username,"hezron")
        self.assertEqual(self.new_user.password,"ngoma123")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(user.user_list),1)


class TestCredetial(unittest.TestCase):
    def setUp(self):
        self.new_credential = credential("hezzykialo","twitter","kialo", "ngoma123")
    

    def test_init(self):
        self.assertEqual(self.new_credential.userName, "hezzykialo")
        self.assertEqual(self.new_credential.siteName, "twitter")
        self.assertEqual(self.new_credential.accountName, "kialo")
        self.assertEqual(self.new_credential.password, "ngoma123")


    def test_save_credentials(self):
        '''
        test to check if the new credential info are saved into the credentials_list
        '''

        self.new_credential.save_credentials()
        twitter = credential("hezzykialo","twitter","hezzy","ngoma123")
        twitter.save_credentials()
        self.assertEqual(len(credential.credentials_list),1)



    def tearDown(self):
        '''
	 	Function to clear the credentials list after every test
	 	'''

        credential.credentials_list = []
        user.user_list = []
		




if __name__ == '__main__':
	unittest.main()

	