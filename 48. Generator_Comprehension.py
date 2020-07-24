# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:18:03 2019

@author: progr
"""
import time
# =============================================================================
# listComprehension=[i**2 for i in range(1,11)]
# print(listComprehension)
# =============================================================================
#IN Generator Comprehension No need yield


# =============================================================================
# generatorComprehension=(i**2 for i in range(1,11))
# for i in generatorComprehension:
#     print(i)
#
# for i in generatorComprehension:
#     print(i)
# =============================================================================

print("List Comprehension")
t1=time.time()
myList=[i**2 for i in range(10000000)]
t2=time.time()
print(t2-t1)

print("\n Generator Comprehension")
t3=time.time()
Generator_Comprehension=(i**2 for i in range(10000000))
t4=time.time()
print(t4-t3)
















