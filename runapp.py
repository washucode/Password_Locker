#!/usr/bin/env python3.6
from usercredentials import users, Credentials
def create_user(fname,sname,uname,password):
    '''
    Function to create a new user
    '''
    new_user = users(fname,sname,uname,password)
    return new_user

def store_user(user):
    '''
    Function to save user
    '''
    users.store_user(user)

def  user_exists(username,password):
    '''
    Function that checks if user exits
    '''
    return Credentials.user_exists(username,password)

def create_credential(username,password,account_name):
    '''
    Function that creates credential
    '''
 
    return Credentials(username,password,account_name)

def  save_credential(credential):
    '''
    Function that saves new credential
    '''
    credential.save_credential()

def generate_password():
    '''
    Function that generates random password
    '''
    return Credentials.generate_password()

def display_credentials():
    '''
    Function that displays credential
    '''
    return Credentials.display_credentials()

def find_by_account(name):
    '''
    Function that finds credential by account name
    '''
    return Credentials.find_by_account(name)

def remove_credential(credential):
    '''
    Function that deletes credential
    '''
    credential.remove_credential()

def main():
    print('-'*100)
    print('Welcome to Password Locker')
    print('-'*100)
    while True:
        print("Use these codes :\n cc-create account \n lg- To login, \n ex- exit password Locker")
        short_code = input().lower().strip()
        if short_code == 'cc':
            print("Create Password Locker Account:")
            firstname = input("Enter your firstName: ").strip()
            secondname = input("Enter your secondName: ").strip()
            username = input("Enter desired username: ").strip()
            password = input("Enter desire password locker password: ").strip()
            store_user(create_user(firstname,secondname,username,password))
            print("\n")
            print (f" Password Locker created for : {firstname} {secondname} with username : {username} and password: {password}")
            print("-"*80)
        elif short_code == 'lg':
            
            username = input('Enter Your Username:')
            password = input('Enter Your Password:')
            userexists = user_exists(username,password)
            if userexists == username:
                print(f"Welcome {username} Choose code to continue")
                while True:
                    print('*'*80)
                    print('Code:\n cc - Create new credential \n ds- display credentials \n de - delete credential ex- Exit')
                    short_code = input().lower().strip()
                    if short_code == 'cc':
                        print('Enter credential details')
                        name = input('Enter account name eg:twitter:').strip()
                        username = input('Enter username for account:').strip()
                        while True:
                            print('\n')
                            print('Choose option:\n gn for generate password \n en to enter your own password')
                            option = input().lower().strip()
                            print('*'*80)
                            if option == 'gn':
                                
                                password = generate_password()
                                break
                            elif option == 'en':
                                password = input('Enter Password:').strip()
                                break
                            else:
                                print("Option Does not Exist.Try Again")
                        save_credential(create_credential(username,password,name))
                        print("\n")
                        print(f"Credential created with sitename : {name} and username : {username} password:{password}")
                    elif short_code == 'ds':
                        print('\n')
                       
                        if display_credentials():
                             print('Here is a list of your credentials')
                             for credential in display_credentials():
                                 print(f"User Name:{credential.username}  Password: {credential.password}  AccountName:{credential.account_name}")
                        else:
                          print("You don't have any credentials saved")
                    elif short_code == "de":
                        print ("Enter account name of the credential you want to delete: ")
                        searchaccount = input()
                        if find_by_account(searchaccount):
                            
                            searchaccount = find_by_account(searchaccount)
                            remove_credential(searchaccount)

                            print("Account Deleted")

                            
                        else :
                            print("That contact does not exist")
                    elif short_code == 'ex':
                        print(f"Bye {username}")
                        break
            else:
                print("Login credentials are not right.Try again")
        elif short_code == 'ex':
            print ("Bye")
            break
if __name__ == "__main__" :
    main()