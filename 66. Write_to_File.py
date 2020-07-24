# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:20:42 2019

@author: progr
"""
#write
with open ("file2.txt","w") as f:
    f.write("Hi my name is zakir")

#append    
with open("file2.txt","a") as ap:
    ap.write("I am a programmer")
