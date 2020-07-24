# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 13:51:26 2019

@author: zakir
"""

myList1=[2,4,6,8,10]
myList2=[2,4,6,7,8,10]

print(all(map(lambda a:a%2==0,myList1)))
print(all(map(lambda a:a%2==0,myList2)))
print(any(map(lambda a:a%2!=0,myList2)))


