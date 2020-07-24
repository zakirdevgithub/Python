# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:39:44 2019

@author: progr
"""
def myfunc(a):
    return a**2

l=[1,2,3,4,5,6,7,8,9,10]

def passing(func,myList):
    myL=[ func(i) for i in myList]
# =============================================================================
#     for i in myList:
#         myL.append(func(i))
# =============================================================================
    return myL

print(passing(myfunc,l))


    