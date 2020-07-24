# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:14:44 2019

@author: progr
"""

myDict={i:i**2 for i in range(1,11)}
print(myDict)

myDict={i:("even" if i%2==0 else "odd") for i in range(1,11)}
print(myDict)

string="Bangladesh"
myDict={char:string.count(char) for char in string}
print(myDict)