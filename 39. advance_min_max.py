# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:19:44 2019

@author: Zakir
"""

names=["Zakir","keya","za","k"]

print(min(names, key=len))
print(max(names, key=len))

myList=[
        
        {"name":"zakir", "age":25, "height":5.7},
        {"name":"keya", "age":25, "height":5.2},
        {"name":"b", "age":2, "height":1.5}
        
        ]

print(max(myList, key=lambda item: item.get("age")))
print(min(myList, key=lambda item: item.get("age")))

myDict={       
        "Python":{"skill":"advance","score":95},
        "C++":{"skill":"intermidiate", "score":80},
        "java":{"skill":"advance","score":90}
        
        }

 

print(min(myDict, key=lambda item: myDict[item].get("score")))





















