import os

def Factorial(No):
    fact = 1
    
    for i in range (1,No+1):
        fact = fact * i
    return fact

def main():
    val=int(input("Enter the number to find the factorial : "))
    
    Ret= Factorial(val)
    print("Factorial is : ",Ret)


if __name__ == "__main__":
    main()
    
