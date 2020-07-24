# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 00:28:22 2019

@author: Zakir
"""

def to_power(power):
    def to_number(number):
        print(number**power)
    return to_number

square=to_power(2)
square(5)

cube=to_power(3)
cube(5)
