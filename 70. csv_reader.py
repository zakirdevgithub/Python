# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:18:01 2019

@author: progr
"""

from csv import reader

with open("info.csv","r") as f:
    data=reader(f, delimiter=",")
    for row in data:
        print(row)