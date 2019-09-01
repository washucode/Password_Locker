import pyperclip
global list_user

class users:

    '''
    class to create users and save their information
    '''

    list_user = []
    def __init__(self, firstname, secondname,password):
        '''
         method to initialize properties that each object will hold
        '''
        self.firstname = firstname
        self.secondname = secondname
        self.password = password
    

