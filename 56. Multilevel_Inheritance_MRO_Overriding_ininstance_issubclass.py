# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:48:11 2019

@author:zakir
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
        
        #Phone.__init__(self,name,model,price)
        super().__init__(name,model,price)
        self.ram=ram
        self.rom=rom
        
    def full_name(self): #Overridding
        return f"name: {self.name} \nmodel: {self.model} \nprice: {self._price} \nRam: {self.ram} \nRom:{self.rom}"  

class FlagshipPhone(Smartphone):
    def __init__(self,name,model,price,ram,rom,rear_camera,front_camera):
        
        super().__init__(name,model,price,ram,rom)
        self.rear_camera=rear_camera
        self.front_camera=front_camera
        
    def full_name(self): #Overridding
        return f"name: {self.name} \nmodel: {self.model} \nprice: {self._price} \nRam: {self.ram} \nRom:{self.rom} \nRear Camera: {self.rear_camera} \nFront Camera: {self.front_camera}"                                       
    
        
        

s=Smartphone("LG","G6",54000,4,64)
print(s.full_name())
print("\n")
f=FlagshipPhone("Samsung","S10+",110000,8,128,"12 MP","5 MP")
print(f.full_name())
#print(help(f)) #MRO (Method Resulation Order)
print(isinstance(f,Smartphone))
print(isinstance(f,Phone))
print(isinstance(s,FlagshipPhone))
print(issubclass(Smartphone,Phone))
print(issubclass(Smartphone,FlagshipPhone))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
