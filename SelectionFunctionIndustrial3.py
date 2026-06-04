#user input
#Procedural - coz of def keyword

def CheckEven(num):
    return(num%2 == 0)

def main():
    Value = 0           #by putting default value we assigned default values of the datatype as int
    Ret = False

    print("Enter number : ")
    Value = int(input())


    Ret = CheckEven(Value)
    if(Ret == True):
        print("It is Even")
    else: 
        print("It is Odd")

if __name__ == "__main__":
    main()
