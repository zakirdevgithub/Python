# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:05:09 2019

@author: Zakir
"""

class Phone: 
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self._price=max(price,0)
        
    def full_name(self):
        return f"name: {self.name} \nmodel: {self.model} \nprice: {self._price}"                                         
    def call(self,number):
        return f"calling {number}"
    
    
class Smartphone(Phone):
    def __init__(self,name,model,price,ram,rom):
        
        #Phone.__init__(self,name,model,price)  Uncommon Method
        super().__init__(name,model,price)

    


obj1= Smartphone("Nokia",1100,1000,4,32)
print(obj1.full_name())
print(obj1.call("01789214021"))