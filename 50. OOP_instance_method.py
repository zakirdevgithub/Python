# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:24:00 2019

@author: zakir
"""
class Person:
    def __init__(self,first_name, last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
    def info(self,target):
        return(f"name: {self.first_name} {self.last_name} age: {self.age} life target:{target}")


p1=Person("Zakir","Hossain",25)
p2=Person("Keya","Rahman",24)

print(p1.info("Good Programmer"))
print(p2.info("House Wife"))