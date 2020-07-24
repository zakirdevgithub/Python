# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:21:50 2019

@author: zakir
"""

f=open("file.txt","r")

# =============================================================================
# # tell() method
# print(f"Cursor Position: {f.tell()}")
# print(f.read())
# print(f"Cursor Position: {f.tell()}")
# =============================================================================

# =============================================================================
# #readline()
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(),end='')
# print(f.readline(),end='')
# =============================================================================

#redlines()
print(f.readlines())
f.seek(0)
for line in f.readlines():
    print(line, end='')

print("\n\n")
f.seek(0)
for line in f.readlines()[:4]:
    print(line,end='')
    

print("File name: ", f.name)  
print(f.closed)
f.close()
print(f.closed)





















