# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:24:20 2019

@author: zakir
"""
from csv import writer

with open("csv_write_file.csv","w", newline="") as f:
    data=writer(f)
# =============================================================================
#     data.writerow(["name","email","phone"])
#     data.writerow(["Zakir Hossain","zakirjava@gmail.com","01789214021"])
#     data.writerow(["Jewel Hossain","jewelsust@gmail.com","01760863687"])
# =============================================================================
    
    data.writerows([["name","email","phone"],["Zakir Hossain","zakirjava@gmail.com","01789214021"],["Jewel Hossain","jewelsust@gmail.com","01760863687"]])
