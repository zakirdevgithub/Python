#
# #------------------------- List ---------------------------------
# myList=["Zakir","Shuvo","Rakib"]
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList)
# myList.append("Sabbir")
# print(myList)
# myList.remove("Sabbir")
# print(myList)
# myAnothetList=["Shovon","Mohi","Rasel","Ashraf"]
# myAnothetList.pop()
#
# print(myAnothetList)
# #myAnothetList.clear()
# print(myAnothetList.index("Mohi"))
# copyList=myList.copy()
# print(copyList)
#
# # myList.append(myAnothetList)
# # print(myList)
# # Output: ['Zakir', 'Shuvo', 'Rakib', ['Shovon', 'Mohi', 'Rasel']]
# myList.extend(myAnothetList)
# print(myList)
# # Output: ['Zakir', 'Shuvo', 'Rakib', 'Shovon', 'Mohi', 'Rasel']
#
# myList.insert(0,"Zahid")
# print(myList)
# myList.sort()
# print(myList)
# #Output:['Mohi', 'Rakib', 'Rasel', 'Shovon', 'Shuvo', 'Zahid', 'Zakir']
# myList.reverse()
# print(myList)



#------------------------- Tuple ----------------------------
# myTuple=("zakir","zahid","keya","zakir")
# print(myTuple[0])
# print(myTuple[1])
# print(myTuple[2])
# print(dir(tuple))
# print(myTuple.count("zakir"))
# print(myTuple.index("zakir"))

#------------------------- Dictionary ------------------------
# myDictionary={"dictionary1":{"name":"Zakir", "age":24, "address":("Pabna", "Sylhet")},
#                 "dictionary2":{"name":"Keya", "age":24, "address":"Pabna"}}
#
# print(myDictionary)
# print(myDictionary["dictionary1"]["age"])
# print(myDictionary["dictionary1"]["address"][1])

#------------------------- String ----------------------
# myInfo="Hi my name is Zakir Hossain and i am 24 years öld !"
# myAnotherInfo=myInfo.replace("24","25")
# print(myAnotherInfo)
# print(dir(str))
# print(myInfo.upper())
# print(myAnotherInfo.lower())
# print(myInfo.title())
# print(myInfo.capitalize())
# print(myInfo.casefold())
# print(myInfo.center(60))
# print(myInfo.center(180))
# print( myInfo.count('a'))
# print(myInfo.encode())
# print(myInfo.encode("ascii", "ignore"))
# print(myInfo.encode("ascii","replace"))
# print(myInfo.endswith("old !"))
# #Output: False
# print(myInfo.endswith(" öld ! "))
# #Output: False because space
# print(myInfo.endswith("öld !"))
# #Output: True
# print(myInfo.split(" "))
# string="          my name is zakir     "
# print(string.rstrip())
# print(string.lstrip())
# print(string.strip())
#
# string2=",,,,,,,,,,,,,,,huha&&&&&&aaaaaaaaaaaaaaaa...........aaa"
# string3="############# my name ############### is zakir########"
# d=string2.strip(",.&a")
# print(d)
# print(string.strip("#"))
# print(string.strip(" #"))
#
# txt = "H\te\tl\tl\to"
# x =  txt.expandtabs(0)
# print(txt)
# print(x)
#
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)
#
# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
# x = mySeparator.join(myDict)
# print(x)
#
# txt = "I could eat bananas all day"
# x = txt.partition("bananas")
# y=txt.partition("all")
# print(x)
# print(y)
#
# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines()
# print(x)

name=["Rakib","Shuvo","Sabbir","Zakir","Abdullah","Rasel"]
print(sorted(name))
print(name)
name.sort()
print(name)

name.pop()
print(name)

fruit1=["apple","banana","orange"]
fruit2=["apple","banana","orange"]

print(fruit1==fruit2)
print(fruit1 is fruit2) #check memory address
print(",".join(fruit1))
