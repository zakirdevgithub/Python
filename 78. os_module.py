# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 00:38:43 2019

@author: zakir
"""
import os

#show current directory
print(os.getcwd())

#change directory
os.chdir("E:\Python World\Python")

print(os.getcwd())

os.chdir("E:\Python World\Python\Chapter 12")

print(os.getcwd())

#creae folder
if os.path.exists("OS MODULE"):
    print("already exsits")
else:
    os.mkdir("OS MODULE")

#create file
open("file.txt","a").close() 

#print file path
for item in os.listdir(r"H:/"):
    path=os.path.join(r"H:/"+item)
    print(path)
    
