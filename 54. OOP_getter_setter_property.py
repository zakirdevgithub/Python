# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:50:26 2019

@author: Zakir
"""
class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self._price=max(price,0)
        #self.full_specification=f"name: {self.name}, model: {self.model}, price: {self._price}"
    
    @property
    def full_specification(self):  #getter()
        return f"name: {self.name}, model: {self.model}, price: {self._price}"
    
    @property
    def price(self): #getter
        return self._price
    
    @price.setter
    def price(self,new_price): #setter
        self._price=max(new_price,0)
    
    
p1=Phone("Nokia",1100,-1000)
print(p1.price)
print(p1.full_specification)
        
