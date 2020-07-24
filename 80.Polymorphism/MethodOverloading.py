class Person:
    def __init__(self):
        print("This is Constructor")

    def Func(self, a=None, b=None, c=None):
        self.a=a
        self.b=b
        self.c=c
        if self.a!=None and self.b!=None and self.c!=None:
            print(f"{self.a}  {self.b} {self.c}")
        elif self.a!=None and self.b!=None:
            print(f"{self.a}  {self.b}")
        else:
            print(f"{self.a}")


obj=Person()
obj.Func(10,20,30)
obj.Func(10,20)
obj.Func(10)
