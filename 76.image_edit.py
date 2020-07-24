# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:38:48 2019

@author: progr
"""

from PIL import Image,ImageEnhance,ImageFilter
import os

#img1=Image.open("bird1.jpg")

#convert image

#img1.save("bird1.png")
#img1.save("bird1.pdf")

#Convert all image

#for item in os.listdir():
#    if item.endswith(".jpg"):
#        img1=Image.open(item)
#        fileName,extension=os.path.splitext(item)
#        img1.save(f"{fileName}.png")

#Image Resize
#image_size=(400,370)
#img1.thumbnail(image_size)
#img1.save("bird1.png")

# =============================================================================
# # -------------Sharpness---------------
# img1=Image.open("bird1.jpg")
# enhancer=ImageEnhance.Sharpness(img1)
# enhancer.enhance(5).show()
# 
# =============================================================================

# =============================================================================
# #--------------- Color ---------------
# 
# img2=Image.open("bird2.jpg")
# enhancer=ImageEnhance.Color(img2)
# enhancer.enhance(0).show()
# =============================================================================



# =============================================================================
# #--------------------- Brightness ------------------
# img3=Image.open("bird3.jpg")
# enhancer=ImageEnhance.Brightness(img3)
# enhancer.enhance(4).show()
# =============================================================================


# =============================================================================
# #----------------- Contrast --------------------------
# img1=Image.open("bird1.jpg")
# enhancer=ImageEnhance.Contrast(img1)
# enhancer.enhance(3).show()
# =============================================================================

# =============================================================================
# #image blur
# img1=Image.open("bird1.jpg")
# 
# img1.filter(ImageFilter.GaussianBlur(radius=6)).show()
# =============================================================================














































