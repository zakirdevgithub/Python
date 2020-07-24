# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 02:00:40 2019

@author: progr
"""

myList=["Zakir","Zahid","Keya","Mitu","Setu","Moni","Mamun"]

def func(names):
    for pos,name in enumerate(names):
        print(f"{pos} ----------->{name}")
        
func(myList)

def target_check(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
        
print(target_check(myList,"Setu"))