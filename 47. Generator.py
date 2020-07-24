# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:09:52 2019

@author: Zakir
"""
def even_number(n):
    for num in range(1,n+1):
        yield(num)

numbers= even_number(20)

for number in numbers:
    print(number)

for number in numbers:
    print(number)
    
