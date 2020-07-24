class Person:
    def walk(self):
        print("Walk Method From Person")

class Zakir(Person):
    def walk(self):
        print("Walk Method From Zakir")

obj=Zakir()
obj.walk()