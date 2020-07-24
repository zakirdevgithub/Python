# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:29:15 2019

@author: progr
"""

from csv import DictReader, DictWriter

with open("csv_DictWriter.csv","r") as rf:
    with open("final.csv", "w",newline="") as wf:
        read_data=DictReader(rf)
        write_data=DictWriter(wf, fieldnames=["name","email","password"])
        write_data.writeheader()
        for row in read_data:
            name,email,password=row["name"],row["email"],row["password"]
            write_data.writerows([{"name":name, "email":email, "password":password}])