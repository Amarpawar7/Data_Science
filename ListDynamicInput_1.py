def main():
    Size = 0
    Size = int(input("Enter the number of elements : "))

    Data = list()
    val=0
    print("Enter the elements : ")
    for i in range(Size):
        val = int(input())
        Data.append(val)           # We prefer this coz in python memory alloaction is done when it is required  
        #Data(i)=val
    print(Data)

if __name__ == "__main__" :
    main()   
