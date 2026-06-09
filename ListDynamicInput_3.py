def Summation(Arr):                               #Parameters can be either list / tuple
    sum=0

    for i in range(len(Arr)):
        sum = sum + Arr[i]
    return sum

def main():
    Size = 0
    Size = int(input("Enter the number of elements : "))

    Data = list()
    val = 0
    print("Enter the elements : ")
    for i in range(Size):
        val = int(input())
        Data.append(val)
        
    Ret = 0
    Ret = Summation(Data)
    print("Summation of all the elements is : ",Ret)   

if __name__ == "__main__" :
    main()   

