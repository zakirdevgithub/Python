
#Normal Method
make_square=[]
for i in range(1,11):
    make_square.append(i**2)
print(make_square)

#list_comprehension

make_square1=[i**2 for i in range(1,11)]
print(make_square1)

#[[1,2,3],[1,2,3],[1,2,3]]

#Normal Method
nested_list=[]
inside_list=[]
for i in range(1,4):
    inside_list.append(i)
for j in range(1,4):
    nested_list.append(inside_list)

print(inside_list)
print(nested_list)

# list_comprehension

nested_list1=[[i for i in range(1,4)] for j in range(1,4)]
print(nested_list1)

# list comprehension with if statement
even_number=[i for i in range(1,11) if i%2==0]
print(even_number)

# list comprehension with if , else statement

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_odd=[i if i%2==0 else -i for i in numbers]
print(even_odd)

# =============================================================================
# for i in numbers:
#     if i%2==0:
#         even_odd.append(i)
#     else:
#         even_odd.append(-i)
# print(even_odd)
# =============================================================================
