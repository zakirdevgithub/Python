# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:46:05 2019

@author: zakir
"""
class Mobile:
    
    dicount_percentage=10
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    @staticmethod
    def hello():
        print("Hello people")
    
    @classmethod
    def class_method(cls,model):
        
        cls.model=model
        print(f" Model: {cls.model}")
        

Mobile.class_method("s8")
Mobile.hello()