# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 03:19:30 2019

@author: zakir
"""

l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
l4=[10,11,12]

new_list=list(zip(l1,l2))
print(new_list)


average=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]  
print(average(l1,l2,l3,l4))