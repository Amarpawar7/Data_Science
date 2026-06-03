#user input
#Procedural - coz of def keyword

def CheckEven(num):
    if(num%2 == 0):
        return True
    else:
        return False

def main():
    Value = 0           #by putting default value we assigned default values of the datatype as int
    Ret = False
    print("Enter number : ")
    Value = int(input())


    Ret = CheckEven(Value)
    print(Ret)

if __name__ == "__main__":
    main()
