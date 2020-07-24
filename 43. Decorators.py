# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 03:54:07 2019

@author: Zakir
"""
from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        print("This is Wrapper Function")
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def func1():
    print("This is Func1")
    
def func2(a,b):
    print("This is Func2")
    print(a+b)


func1()
func2(100,200)






















