def Multiplication (Value1, Value2):
    Ans=0           #Local Variable : variable declared inside the function
    Ans = Value1 * Value2
    return Ans

no1 = 0            #Global variable : variable declared outside the function 
no2 = 0
Result = 0 

no1= int(input("Enter first number : "))
no2= int(input("Enter second number : "))

Result = Multiplication(no1,no2)
print("Multiplication is : ",Result)

################################################3

no1= int(input("Enter first number : "))
no2= int(input("Enter second number : "))

Result = Multiplication(no1,no2)
print("Multiplication is : ",Result)

