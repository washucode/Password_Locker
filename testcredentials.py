import unittest
from usercredentials import users, Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Create user before every test
        '''
        self.new_user = users('James','Muruiki','jmanes','paswkort')
    
    def test__init__(self):
        '''
        test that initialization was done well
        '''
        self.assertEqual(self.new_user.firstname,'James')
        self.assertEqual(self.new_user.secondname,'Muruiki')
        self.assertEqual(self.new_user.password,'paswkort')
        self.assertEqual(self.new_user.username,'jmanes')
    
    def test_store_user(self):
        self.new_user.store_user()
        self.assertEqual(len(users.list_user),1)

    def tearDown(self):
        ''' 
        to undo the tests before this
        '''
        users.list_user=[]



class  TestCredentials (unittest.TestCase):

    

    def setUp(self):
        self.new_credential = Credentials('marym','dapdjaojd','twitter')
    
    def test__init(self):
        self.assertEqual(self.new_credential.username,'marym')
        self.assertEqual(self.new_credential.password,'dapdjaojd')
        self.assertEqual(self.new_credential.account_name,'twitter')
    def test_user_exists(self):
        self.new_user = users('James','Muruiki','jmanes','paswkort')
        self.new_user.store_user()

        for user in users.list_user:
            if(user.username==self.new_user.username and user.password == self.new_user.password):
                userlogin = user.username
            return userlogin

    def test_save_credentials(self):
        '''
        test if programme can save credentials
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.account_credentials),1)
    
    def test_generate_userpassword(self):
        generate_password = Credentials.generate_password(self,10)
        self.assertTrue(generate_password)
    
    def test_display_credentials(self):
         
        self.assertEqual(Credentials.display_credentials(),Credentials.account_credentials)
    
    def tearDown(self):
        Credentials.account_credentials = []
    def test_findbyaccount(self):
        '''
        test if credentials can be found using their account name
        '''
        self.new_credential.save_credential()
        newTestcredential = Credentials('Doe','does','facebook')
        newTestcredential.save_credential()
        foundcredential = Credentials.find_by_account('facebook')
        self.assertEqual(foundcredential,newTestcredential)
    
    def test_removecredential(self):
        '''
        test if credential can be removed
        '''
        self.new_credential.save_credential()
        newTestcredential = Credentials('Doe','does','facebook')
        newTestcredential.save_credential()
        newTestcredential.remove_credential()
        self.assertEqual(len(Credentials.account_credentials),1)
    




if __name__ == '__main__':
    unittest.main()
    
    
    
    
    