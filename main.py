#! /usr/bin/env python3.9

from user_class import user
from credetial_class import credential


def create_user(username, password):
	'''
	Function to create a new user account
	'''
	new_user = user(username,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	user.save_user(user)

def verify_user(userName,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = credential.check_user(userName,password)
	return checking_user

def create_credential(userName,siteName,accountName,password):
	'''
	Function to create a new credential
	'''
	new_credential= credential(userName,siteName,accountName,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	credential.save_credentials(credential)



def display_credentials(userName):
	'''
	Function to display credentials saved by a user
	'''
	return credential.display_credentials(userName)