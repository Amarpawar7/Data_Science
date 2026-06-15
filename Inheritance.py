class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
        self.No1 = 10
        self.No2 = 20

    def fun(self):
        print("Inside fun method of Parent")
        
class Child(Parent):
    def __init__(self):
        super().__init__()                                        # super keyword is ud=e=sed to acces method from parent class
        print("Inside Child constructor")
        self.A = 11
        self.B = 21
    
    def sun(self):
        print("Inside sun method of child")

cobj = Child()
