#Filter ,map and reduce

from functools import reduce

CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : No + 1
Add=lambda A,B : A+B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)

    FData=list(filter(CheckEven , Data))               #typecasting is done to assign it as list,or else ID of FData will be displayed
    print("Data after filter is : ",FData)

    MData = list(map(Increment ,FData))
    print("Data after map is : ",MData)

    RData = reduce(Add , MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()
    
    
