def main():
    Size = 0
    Size = int(input("Enter the number of elements : "))

    Data = list()
    val=0
    print("Enter the elements : ")
    for i in range(Size):
        val = int(input())
        Data.append(val)          

    sum=0

    for i in range(Size):
        sum = sum + Data[i]
    
    print("Summation of all the elements is : ",sum)   

if __name__ == "__main__" :
    main()   
