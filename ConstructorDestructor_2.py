import gc            # gc = garbage collector
 
class Demo : 
    def __init__(self):                    #call goes to init as soon as object is formed
        print("Inside Constructor! ")

    def __del__(self):
        print("Inside Destructor! ")

# Allocate
obj1 = Demo()
obj2 = Demo()

# Use

# Deallocate
del obj1
del obj2

gc.collect()

print("End of application")
