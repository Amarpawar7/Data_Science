#Filter ,map and reduce
#lambda function is used in FMR

from functools import reduce

def main():

    # user input can be written here
    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)

    FData=list(filter((lambda No : (No % 2 == 0)), Data))               #typecasting is done to assign it as list,or else ID of FData will be displayed
    print("Data after filter is : ",FData)

    MData = list(map((lambda No : No + 1),FData))
    print("Data after map is : ",MData)

    RData = reduce((lambda A,B : A+B), MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()
    
