# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:07:36 2019

@author: Zakir
"""

from functools import wraps
def decorator_function(function):
    @wraps(function)
    def wrapper_function(*args,**kwargs):
        print(f"This is from {function.__name__} function")
        print(f"Doc is {function.__doc__}")
        
        return function(*args,**kwargs)
    return wrapper_function

@decorator_function
def add(a,b):
    """ This function takes two argument and give addition of two numbers"""
    return a+b
print(add(100,200))
    
        
        
