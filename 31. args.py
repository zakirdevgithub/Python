# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:42:28 2019

@author: progr
"""

# =============================================================================
# def func(a,b):
#     print(a+b)
# 
# func(10,20) #Fine
# #func(10,20,30,40,50) error because many argument
# 
# 
# 
# =============================================================================

def func(*args):
    total=0
    for i in args:
        total+=i
    return total

print(func(10,20,30,40,50))


def func2(num,*args):
    total=0
    print(num)
    for i in args:
        total+=i
    return total

print(func2(1,2,3,5))

def func3(num1,num2,*args):
    total=0
    print(num1)
    print(num2)
    for i in args:
        total+=i
    return total

print(func3(1,2,3,5))


def func4(*args):
    for i in args:
        print(i)


myList=["Zakir","Jewel","Keya"]

func4(myList)
func4(*myList) #unpacking


def func5(*args):
    total=0
    for i in args:
        total+=i
    print(total)
    
myTuple=(100,200,300,400,500)
#func5(myTuple) error
func5(*myTuple) #unpacking














