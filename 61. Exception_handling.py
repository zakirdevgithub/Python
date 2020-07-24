# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 00:23:40 2019

@author: zakir
"""
myBool=True
while myBool:
    try:
        age=int(input("Enter your age: "))
    
    except ValueError:
        print("INPUT a integer number. You may input string....")
    except:
        print("UnexpectedError")
    else:
        print("This will execute when try is not error")
        if age<18:
             print("You can't play this game")
        else:
             print("You can Play this game")
        break
    finally:
        print("Enjoy this Game")


        


        
    
    
        
