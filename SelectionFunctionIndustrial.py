#user input
#Procedural - def keyword

def CheckEven(num):
    if(num%2 == 0):
        return True
    else:
        return False

def main():
    Value = 0           #by puting default value we assigned default values of the datatype as int
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



