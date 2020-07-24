myDict={"name":"Zakir","age":24,"programming":{"python":"advanced","C++":"advanced","java":"advanced"}}
# for key in myDict.keys():
#     print(key)
# for value in myDict.values():
#     print(value)
# for key,value in myDict.items():
#     print(key, end=" ")
#     print(value)
# myDict["age"]=25
# for key,value in myDict.items():
#     print(key, end=" ")
#     print(value)
# myUpdateDict={"name":"Zakir","age":25,"Sector":{"sector1":"Data scientist","sector2":"Game developer","sector3":"Web developer"}}
# myDict.update(myUpdateDict)
# print(myDict)

#Add
myDict["fav_movie"]=["Superman","Batman","Iron Man"]
print(myDict)

#Delete

popped_item=myDict.pop("fav_movie")
print(popped_item)
print(myDict)

#Delete Randomly

popped_Random= myDict.popitem()
print(popped_Random)
print(myDict)
