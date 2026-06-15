class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
        

    def fun(self):
        print("Inside fun method of Parent")
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child constructor")
        
    def fun(self):
        super().fun()                               # This will call fun function from Parents class
        print("Inside fun method of Child")

cobj = Child()

cobj.fun()         # as object is of Child class

