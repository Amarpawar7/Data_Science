import gc            # gc = garbage collector
 
class Demo : 
    def __init__(self):                    #call goes to init as soon as object is formed
        print("Inside Constructor! ")

    def __del__(self):
        print("Inside Destructor! ")

# Allocate
obj = Demo()

# Use

# Deallocate
del obj

gc.collect()

print("End of application")
