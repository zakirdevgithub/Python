

s1={1,2,3,4,4,4,5,5,5,7,8,9}
print(s1)
s1.add(12)
s1.add(23)
s1.add("Zakir")
print(s1)
s1.remove(23)
print(s1)
# s1.remove(50) error
s1.discard(12)
print(s1)
s1.discard(50)
print(s1)
l=[1,4,5,6,7,7,7,8,8,9]
s2=list(set(l))
print(s2)

s3={1,3,5}
s4={2,4,6}
s5={1,5,8,9}
print(s3|s4) #Union
print(s3&s4) #intersection
print(s3&s5)
