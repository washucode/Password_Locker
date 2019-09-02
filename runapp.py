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
    Credentials.save_credential()

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

def find_by_account():
    '''
    Function that finds credential by account name
    '''
    return Credentials.find_by_account()

def remove_credential():
    '''
    Function that deletes credential
    '''
    Credentials.remove_credential()

def main():
    print('-'*100)
    print('Welcome to Password Locker')
    print('-'*100)
    print("Create Password Locker Account:")
    firstname = input("Enter your firstName: ").strip()
    secondname = input("Enter your secondName: ").strip()
    username = input("Enter desired username: ").strip()
    password = input("Enter desire password locker password: ").strip()
    store_user(create_user(firstname,secondname,username,password))
    print("\n")
    print (f" Password Locker created for : {firstname} {secondname} with username : {username} and password: {password}")
    print("-"*80)
if __name__ == "__main__":
    main()