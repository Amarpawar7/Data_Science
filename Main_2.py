def Multiplication (Value1, Value2):
    Ans=0           #Local Variable: variable declared inside the function
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

#Starter
if __name__ == "__main__":
    main()



