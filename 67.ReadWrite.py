# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:26:11 2019

@author: zakir
"""
with open ("file2.txt","r+") as f:
    print(f.read())
    f.write(" I am also a Gamer") #append
    print(f.read())
