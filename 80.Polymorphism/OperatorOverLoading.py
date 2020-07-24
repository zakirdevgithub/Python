class Operator:
    def __init__(self,num1,num2, num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3


    def __add__(self, other):
        m1= self.num1+other.num1
        m2=self.num2+other.num2
        m3=self.num3+other.num3
        return m1+m2+m3
    def __gt__(self, other):
        if self.num1 > other.num1:
            return True
        else:
            return False


obj= Operator(10,20,30)
obj2=Operator(100,200,300)
obj3=obj+obj2
print(obj3)

print(obj>obj2)
