#!/usr/bin/env python3.6
from usercredentials import users, Credentials
def create_user(fname,sname,uname,password):
    '''
    Function to create a new user
    '''
    new_user = users(fname,sname,uname,password)
    return new_user

