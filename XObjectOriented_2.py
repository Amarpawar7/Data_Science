class Arithematic:
    def Addition (self,a,b):
        return a+b

    def Substraction(self,a,b):
        return a-b

No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

obj = Arithematic()                               # we created object for our class
Ans = obj.Addition(No1,No2)                      
print("Addition is : ",Ans)

Ans = obj.Substraction(No1,No2)                          # this is caalled as instance meathod
print("Substraction is : ",Ans)

