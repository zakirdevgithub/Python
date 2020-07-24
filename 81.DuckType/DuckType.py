class QT:
    def Can(self):
        print("Develop App with C++")
        print("Develop App With Python")

class IntelliJ:
    def Can(self):
        print("Develop App with Java")

class User:
    def Func(self,ide):
        ide.Can()

ide=QT()
ide2=IntelliJ()
obj=User()
obj.Func(ide)
obj.Func(ide2)



