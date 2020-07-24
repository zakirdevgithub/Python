# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:01:35 2019

@author: progr
"""

class Circle:
    pi=3.1416
    
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return(Circle.pi*self.radius*self.radius)
        
    def circumference(self):
        return(2*Circle.pi*self.radius)
        
        
obj=Circle(5)

print(obj.area())
print(obj.circumference())

