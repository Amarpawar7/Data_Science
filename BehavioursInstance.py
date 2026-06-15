class Demo : 
    No = 10                                                                         # Class Variable
    
    def __init__ (self,A,B):  
        self.Value1 = A                                                             # Instance Variable
        self.Value2 = B

    def fun(self):
        print("Inside instance method fun ! ",self.Value1 , self.Value2)            # Instance method
    

    @classmethod                                                                    # Decorator
    def sun(cls):
        print("Inside class method sun ! ",cls.No)                                  # Class method

Demo.sun()

print("Class variable : ",Demo.No)

obj = Demo(11,21)

obj.fun()

print("Instance Variable : ",obj.Value1 , obj.Value2)
