import gc            # gc = garbage collector
 
class Demo : 
    # Class Variable
    No1 = 10                         # these are class variables so we didn't use object to access these variables not instance variables
    No2 = 11

    def __init__(self):                    #call goes to init as soon as object is formed
        # Instance variable
        self.A = 101                                    # we use self keyword to assign a variable as an instance 
        self.B = 201
        print("Inside Constructor! ")

    def __del__(self):
        print("Inside Destructor! ")

print(Demo.No1)                          # to access class variable we use class name
print(Demo.No2)

obj = Demo()                              # to access an instance variable we need to make an object

print(obj.A)
print(obj.B)

