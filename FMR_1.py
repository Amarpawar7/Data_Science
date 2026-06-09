# Filter , Map , Reduce

def CheckEven(No):
    return (No % 2 == 0)


def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)

    FData=list(filter(CheckEven , Data))               #typecasting is done to assign it as list,or else ID of FData will be displayed
    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()
    
