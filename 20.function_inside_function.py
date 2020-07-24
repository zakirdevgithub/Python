
def greater(a,b):
    if a>b:
        return a
    else:
        return b

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
def greatest(a,b,c):
    bigger=greater(a,b)
    return greater(bigger,c)
print(greater(10,20))
print(greatest(10,20,30))
