# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:36:52 2019

@author: Zakir
"""
from functools import wraps

def only_allow_data_type(data_type):
    def decorator_function(function):
        @wraps(function)
        def wrapper_function(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args,**kwargs)
            return ("Invalid Argument")
        return wrapper_function
    return decorator_function

@only_allow_data_type(str)
def func1(*args):
    string=""
    for arg in args:
        string +=arg
    return string

#print(func1("Zakir"," Hossain"," is"," a"," Good"," Programmer",9))
print(func1("Zakir"," Hossain"," is"," a"," Good"," Programmer"))











































