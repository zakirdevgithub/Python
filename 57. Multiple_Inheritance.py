# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:08:46 2019

@author: zakir
"""

class A:
    def class_a_method(self):
        return f"I am from Class A"
    def hello(self):
        return "hello from A"
    

class B:
   def class_b_method(self):
        return f"I am from Class B"
   def hello(self):
        return "hello from B"  
    
#class C(A,B):
#    pass

class C(B,A):
    pass


object_c=C()
print(object_c.class_a_method())
print(object_c.class_b_method())
#print(object_c.hello()) # because C(A,B)
print(object_c.hello()) #because C(B,A)
print(C.__mro__)






























