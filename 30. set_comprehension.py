# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:38:38 2019

@author: progr
"""
mySet={i**2 for i in range(1,11)}
print(mySet)

myList=["Zakir","Jewel","Keya"]
mySet={name[0] for name in myList}
print(mySet)
