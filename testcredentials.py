import unittest
from usercredentials import users

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Create user before every test
        '''
        self.new_user = users('James','Muruiki','paswkort')
    
    def test__init__(self):
        '''
        test that initialization was done well
        '''
        self.assertEqual(self.new_user.firstname,'James')
        self.assertEqual(self.new_user.secondname,'Muruiki')
        self.assertEqual(self.new_user.password,'paswkort')git 

if __name__ == '__main__':
    unittest.main()
    
    
    
    
    