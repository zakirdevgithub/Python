# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:50:44 2019

@author: Zakir
"""

mList=["Zakir","Keya","Mitu","Setu"]

mList.sort()
print(mList)

mTuple=("Zakir","Keya","Mitu","Setu")

# =============================================================================
# mTuple.sort()
# print(mTuple)   ERROR
# =============================================================================
print(sorted(mTuple))

mSet={"Zakir","Keya","Mitu","Setu"}

# =============================================================================
# mSet.sort()
# print(mSet)  ERROR
# =============================================================================
print(sorted(mSet))

myList=[
        
        {"name":"zakir", "age":25, "height":5.7},
        {"name":"keya", "age":24, "height":5.2},
        {"name":"b", "age":2, "height":1.5}
        
        ]

print(sorted(myList, key=lambda item: item.get("age")))


myDict={       
        "Python":{"skill":"advance","score":95},
        "C++":{"skill":"intermidiate", "score":80},
        "java":{"skill":"advance","score":90}
        
        }
print(sorted(myDict, key=lambda item:myDict[item].get("score")))
















