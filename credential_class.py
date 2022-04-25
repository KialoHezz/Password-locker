from user_class import User  
class credential:
	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	# Class Variables
	credentials_list =[]

	
	@classmethod
	def check_user(cls,username,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		user=User
		current_user = ''
		for user in user.users_list:
			if (user.username == username and user.password == password):
				current_user = user.first_name
		return current_user

	def __init__(self,userName,siteName,accountName,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = userName
		self.site_name = siteName
		self.account_name = accountName
		self.password = password


	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
		# global users_list
		credential.credentials_list.append(self)
	


	@classmethod
	def display_credentials(cls,user_name):
		'''
		Class method to display the list of credentials saved
		'''
		user_credentials_list = []

		for credential in cls.credentials_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list
				

	
	@classmethod
	def find_by_site_name(cls, site_name):
		'''
		Method that takes in a site_name and returns a credential that matches that site_name.
		'''
		for credential in cls.credentials_list:
			if credential.site_name == site_name:
				return credential