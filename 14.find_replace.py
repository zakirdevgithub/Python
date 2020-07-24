sentence="Bangladesh is a beautiful country. It is a developing country"
print(sentence.find("is"))
print(sentence.find("is",12))
print(sentence.find("country"))
country_pos_first=sentence.find("country")
print(sentence.find("country",country_pos_first+1))

print(sentence.replace("is","was"))
print(sentence.replace("is","was",1))
print(sentence.replace("country","desh",1))
