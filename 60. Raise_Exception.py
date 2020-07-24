# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:22:09 2019

@author: zakir
"""

# =============================================================================
# def add(a,b):
#     if ((type(a) is int) and (type(b) is int)):
#         print (a+b)
#     else:
#         raise TypeError("Please input int type")
#         
# add('5','6')
# =============================================================================

#Abstract Method

class Animal:
    def __init__(self,name):
        self.name=name
        
    def sound(self):
        raise NotImplementedError("You need define sound class in subclass")
    
    
class Dog(Animal):
    def __init__(self,name,voice):
        super().__init__(name)
        self.voice=voice
    
    def sound(self):
        return "Ghew Ghew"
    
    
class Cat(Animal):
    def __init__(self,name,voice):
        super().__init__(name)
        self.voice=voice
    
    def sound(self):
        return "Meao Meeao"   
    
dog=Dog("DOG","Ghew")
print(dog.sound())



class Phone:
    def __init__(self,name):
        self.name=name

        
class Smartphone:
    def __init__(self):
        self.mobiles=[]
    
    def add_mobile(self,new_mobile):
        if(isinstance(new_mobile,Phone)):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("Type error")
            
lg=Phone("LG")
samsung=Smartphone()
print(lg.name)
samsung.add_mobile(lg)
print(samsung.mobiles[0].name)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    