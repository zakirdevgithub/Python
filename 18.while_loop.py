import random
number=1
while not number ==10:
    print(number)
    number +=1;


while True:

    guess=int(input("Enter your gussing number: "))
    num=random.randint(1,10)
    if guess==num:
        break
    else:
        print("You Faild")

print("Congratulations You Win")
