# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:41:36 2019

@author: progr
"""

from csv import DictWriter

with open("csv_DictWriter.csv", "w", newline="") as f:
    data=DictWriter(f, fieldnames=["name","email","password"])
    data.writeheader()
# =============================================================================
#     data.writerow({"name":"Zakir Hossain","email":"zakirjava@gmail.com","password":"1234567"})
#     data.writerow({"name":"Jewel Hossain","email":"jewelsust@gmail.com","password":"1234abcd"})
# =============================================================================
    data.writerows([
            {"name":"Zakir Hossain","email":"zakirjava@gmail.com","password":"1234567"},
            {"name":"Jewel Hossain","email":"jewelsust@gmail.com","password":"1234abcd"}
            ])