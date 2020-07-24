# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:08:32 2019

@author: zakir
"""

class Mobile:
    discount_percentage=10
    
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
        
    def mobile_info(self):
        print(f"Brand Name:{self.name} , Model: {self.model}, Original Price:{self.price}, Price with Discount:{((100-self.discount_percentage)*self.price)/100}")

samsung=Mobile("Samsung","S10+",120000)
samsung.discount_percentage=20      
samsung.mobile_info()   
print("\n")
iphone=Mobile("iPhone","Xmax",120000)
iphone.discount_percentage=5
iphone.mobile_info()                                                  
        
