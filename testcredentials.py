import unittest
import pyperclip
from usercredentials import users

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Create user before every test
        '''
        self.new_user = users('James','Muruiki','paswkort')
    
    
    
    