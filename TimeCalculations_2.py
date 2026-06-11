import time
def Factorial(No):
    fact = 1
    for i in range (1,No+1):
        fact = fact * i
    return fact

def main():
    val=int(input("Enter the number to find the factorial : "))
    start_time = time.time()
    Ret= Factorial(val)
    end_time = time.time()
    print("Factorial is : ",Ret)
    print("Total Exection time : ",end_time - start_time)
if __name__ == "__main__":
    main()
    
