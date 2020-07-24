# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 00:54:00 2019

@author: zakir
"""

class NumberTypeError(ValueError):
    pass

def validateNumber(number):
    if number<18:
        raise NumberTypeError("You enter a invalid number")
        
number=int(input("Enter a number: "))
validateNumber(number)