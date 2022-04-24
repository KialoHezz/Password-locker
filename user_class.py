class user:
    '''
    variable to store the users
    '''
    user_list = []

    def __init__(self,username,password):
        '''
        Instance variables as assigned username and password
        '''
        self.username = username
        self.password = password
    
    def save_user(self,user):
        user.user_list.append(self)