#! /usr/bin/env python3.9

from user_class import user
from credential_class import credential


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


def main ():
    print('Please enter your name:')
    use_name = input()

    print(f'Hello! {use_name} Welcome to password locker')

    while True:
        print('Use these codes to navigate: \n CA-Create an Account \n LI-Log In \n EX -Exit')
        short_code = input('Enter your choice:').lower()


        if short_code == "ca":
            print("Create new account:")
            username = input("Enter your username ")
            password = int(input("Your password:"))
            save_user(create_user(username,password))

            print(f'New account for : {username}  created successfully ')
        
        elif short_code == "li":
            print("Loging into existing account to our system:")

            username = input('Enter your first name - ')
            password = input('Enter your password - ')

            user_exists = verify_user(username,password)

            if user_exists == username:
                print(f'Welcome {username}. Please choose an option to continue.')

                while True:
                    print('Use these codes to navigate: \n  CC- copy \n EX -Exit')
                    short_code = input('Enter your choice:').lower()
					
                    if short_code  == 'cc':
                        print('Enter your credential details:')


                        userName = input('enter the username')
                        siteName = input('Enter the site name- ')
                        accountName = input('Enter your account  name - ')

                        save_credential(create_credential(userName,siteName,accountName,password))
                        print(f'Credential Created: Site Name: {siteName} - Account Name: {accountName} - Password: {password}')
                    
                    elif short_code == "ex":
                        print(f'Goodbye {username}')

                    else:
                        print('Oop! Wrong details entered . Try again or Creae another account' )

        elif short_code == "ex":
            print(f'Goodbye {use_name}')

        
        else:    
            print('Oops! Wrong option entered. Try again.')



if __name__ == '__main__':
	main()