def Multiplication (Value1, Value2):
    Ans=0           #Local Variable: variable declared inside the function and the once defined outside the function are global variable
    Ans = Value1 * Value2
    return Ans

def main():
    no1 = 0
    no2 = 0
    Result = 0 

    no1= int(input("Enter first number : "))
    no2= int(input("Enter second number : "))

    Result = Multiplication(no1,no2)
    print("Multiplication is : ",Result)

main()
