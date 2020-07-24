# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:16:52 2019

@author: progr
"""

from functools import wraps
def input_int_only(function):
    @wraps(function)
    def wrapper_function(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return function(*args,**kwargs)
        else:
            print("Invalid Type")
    return wrapper_function

@input_int_only
def func(*args):
    for arg in args:
        print(arg)
        

func(1,2,3,4,5,[1,2,3,4])
#func(1,2,3,4,5)
















