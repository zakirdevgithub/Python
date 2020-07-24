# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:10:40 2019

@author: progr
"""

def func(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

func(first_name="Zakir", last_name="Hossain")
func(var1=24, var2=25)

myDict={"name":"Zakir","age":24}

func(**myDict)
