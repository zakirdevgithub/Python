# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 04:33:25 2019

@author: zakir
"""

import os
import shutil

file_iterate=os.walk(r"E:/New folder")
for path,folder,file in file_iterate:
    print(f"path: {path}")
    print(f"folder: {folder}")
    print(f"file: {folder}")


#shutil.move("15. IO and Streams","New folder/15. IO and Streams")
#shutil.rmtree("15. IO and Streams")
#shutil.copytree("10. Inheritance","New folder/10. Inheritance")
#shutil.copy("file.txt","New folder/file10.pdf")
