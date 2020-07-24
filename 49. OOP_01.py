# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 02:39:32 2019

@author: zakir
"""

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
p1=Person("Zakir","Hossain",25)
p2=Person("Keya","Rahman",24)

print(p1.first_name)
print(p2.first_name)