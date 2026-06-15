class Demo : 
    No = 10
    
    def __init__ (self,A,B):                       # init is required to create an instance
        self.Value1 = A
        self.Value2 = B

print("Class variable : ",Demo.No)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

# print(obj1.No)                                         # class variable can also be accessed by object ,this is allowed

print("Instance Variables of obj1 : ",obj1.Value1 , obj1.Value2)               # 11 , 21
print("Instance Variables of obj1 : ",obj2.Value1 , obj2.Value2)               # 51 , 101

obj1.Value1 = 15  

Demo.No = 0
# obj1.No = 0

print("Instance Variables of obj1 : ",obj1.Value1 , obj1.Value2)               # 15 , 21
print("Instance Variables of obj1 : ",obj2.Value1 , obj2.Value2)               # 51 , 101

print(obj1.No)                                                                 # 0
print(obj2.No)                                                                 # 0 