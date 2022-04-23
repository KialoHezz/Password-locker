'''
Created user class
'''
from typing_extensions import Self


class user:

    # store the users

    user_list = []
    '''
    created new instance of a class and have passed in properties of the object
    '''
    def __init__(self,username,password):
        '''
        instance variable where they take up - username and password
        '''
        self.username = username
        self.password = password


    '''
    function to save the user in user_list
    '''
    def save_user(self):
        user.user_list.append(self)