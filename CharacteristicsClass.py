import gc            # gc = garbage collector
 
class Demo : 
    # Class Variable
    No1 = 10                         # thers are class variables sos we didn't use object to access these variables not instance variables
    No2 = 11

    def __init__(self):                    #call goes to init as soon as object is formed
        print("Inside Constructor! ")

    def __del__(self):
        print("Inside Destructor! ")

print(Demo.No1)
print(Demo.No2)
