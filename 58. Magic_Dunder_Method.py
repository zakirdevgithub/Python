# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:09:03 2019

@author: zakir
"""
class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    
    def full_name(self):
        return f"name: {self.name} \nmodel: {self.model} \nprice: {self.price}"
# =============================================================================
#     def __repr__(self):
#         return f"Phone(\"{self.name}\",\"{self.model}\",{self.price})"
# =============================================================================
    
    def __str__(self):
        return f"name: {self.name}, model: {self.model}, price: {self.price}"
    
    def __len__(self):
        return len(self.full_name())
        
        
        
p=Phone("LG","G6",54000)
print(p)
print(len(p))
