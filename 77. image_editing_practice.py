# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:26:19 2019

@author: zakir
"""
from PIL import Image,ImageEnhance, ImageFilter
import os

#Change type

for item in os.listdir():
    if item.endswith(".jpg"):
        img=Image.open(item)
        fileName,extention=os.path.splitext(item)
        img.save(f"{fileName}.pdf")
        img.save(f"{fileName}.png")

#Change size
for item in os.listdir():  
    if item.endswith(".png"):    
        image_size=(20,20)
        img1=Image.open(item)
        img1.thumbnail(image_size)
        fileName,extention=os.path.splitext(item)
        img1.save(f"{fileName}.png")


#------------------- Sharpness -------------

img3=Image.open("bird3.jpg")
enhancer=ImageEnhance.Sharpness(img3)
enhancer.enhance(3).save("new_bird3_Sharpness.jpg")

#--------------------- Color -------------
img4=Image.open("bird3.jpg")
cEnhancer=ImageEnhance.Color(img4)
cEnhancer.enhance(5).save("new_bird3_Color.jpg")

#--------------- Brightness --------------
img5=Image.open("bird3.jpg")
bEnhancer=ImageEnhance.Brightness(img5)
bEnhancer.enhance(6).save("new_bird3_Brightness.jpg")

#-------------- Contrast ---------------
img6=Image.open("bird3.jpg")
conEnhancer=ImageEnhance.Contrast(img6)
conEnhancer.enhance(6).save("new_bird3_Brightness.jpg")

#---------------- GaussianBlur ---------------
img7=Image.open("bird3.jpg")
img7.filter(ImageFilter.GaussianBlur(radius=4)).save("new_bird3_GaussianBlur.jpg")























