# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:30:44 2019

@author: zakir
"""

with open("file2.txt","r") as rf:
    with open("file2.txt","w") as wf:
        wf.write("Hello guys. I am zakir hossain")
    
    print(rf.read())