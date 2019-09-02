import pyperclip
import random
import string
global list_user

class users:

    '''
    class to create users and save their information
    '''

    list_user = []
    def __init__(self, firstname, secondname,username,password):
        '''
         method to initialize properties that each  user object will hold
        '''
        self.firstname = firstname
        self.secondname = secondname
        self.username = username
        self.password = password
    def store_user(self):
        '''
        method to save user
        '''
        users.list_user.append(self)

class Credentials:

    account_credentials = []

    
    
    def __init__(self,username,password,account_name):
        '''
         method to initialize properties that each  credentials object will hold
        '''
        self.username = username
        self.password = password
        self.account_name = account_name

    @classmethod
    def user_exists(cls, username,password):
        '''
        method to check if user exists
        '''
        userlogin = ''
        for user in users.list_user:
            if (user.username == username and user.password == password):
                userlogin = user.username
            return userlogin
    
    def save_credential(self):
        '''
        method to save user credentials
        '''
        Credentials.account_credentials.append(self)
    
    def generate_password(number=10):
        '''
        method to generate random password
        '''
        password_gen = string.ascii_letters + string.digits
        user_password = ''.join(random.choice(password_gen) for i in range(number))
        return user_password
    
    @classmethod
    
    def display_credentials(cls):
        '''
          method to display credentials
        '''
        return cls.account_credentials

    @classmethod
    
    def find_by_account(cls,name):
        '''
        method to helo user find credentials by account
        '''

        for  credential in cls.account_credentials:
            if credential.account_name == name:
                return credential

    
    def remove_credential(self):
        Credentials.account_credentials.remove(self)
