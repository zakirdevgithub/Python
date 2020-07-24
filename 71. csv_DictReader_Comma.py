# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:25:59 2019

@author: progr
"""

from csv import DictReader

with open("info2.csv","r") as f:
    data=DictReader(f, delimiter=",")
    for row in data:
        print(row["name"])
        print(row["email"])
        print(row["phone"])