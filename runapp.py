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
    Functions that generates random password
    '''
    return Credentials.generate_password()

