
#fromkeys(), clear(), get()

myDict={
   "name":"Zakir",
   "age":24,
   "height":5.7
}

print(myDict["name"])
print(myDict.get("names"))
print(myDict.get("names","not found!"))
myDict.clear()
print(myDict)

# myAnotherDict= dict.fromkeys(["name","age"],"unknown")
# print(myAnotherDict)
# myAnotherDict2= dict.fromkeys(["name","age"],["unknown","hablu"])
# print(myAnotherDict2)
# myAnotherDict3= dict.fromkeys(["name","age"],("unknown","hablu"))
# print(myAnotherDict3)
# myAnotherDict4= dict.fromkeys(("name","age"),("unknown","hablu"))
# print(myAnotherDict4)
#
# myAnotherDict5= dict.fromkeys("abc","zakir")
# print(myAnotherDict5)
#
# myAnotherDict6= dict.fromkeys(range(1,21),"zakir")
# print(myAnotherDict6)
