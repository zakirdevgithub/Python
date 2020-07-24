# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:50:08 2019

@author: zakir
"""
with open("emot.txt", "r", encoding="utf-8") as f:
    data=f.read()
    while len(data)>0:
        print(data)
        data=f.read(100)
        
