number=int(input("Enter a number: "))
if number<=100:
    if 0<number<=10:
        print("number range 0 to 10")
    elif 10<number<=20:
        print("number range 10 to 20")
    elif number>20 and number<=30:
        print("number range 20 to 30")
    elif number==50 or number==100:
        print("number is 50 or 100")
    elif number==0:
        pass
else:
    print("please input a number between 0 to 100")

name="Zakir"
if "k" in name:
    print("Zakir contain k")
