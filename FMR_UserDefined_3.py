#Filter ,map and reduce
## No need for Funtools coz we created function for reduce

CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : No + 1
Add=lambda A,B : A+B

def filterX(Task , Elements): 
    Result = list()                # Return = []

    for no in Elements:
        Ret = Task(no)
        if(Ret == True):
            Result.append(no)
    return Result

def mapX(Task , Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

# Add=lambda A,B : A+B

def reduceX(Task , Elements):              #Task : Add    &    Element : [11,21,23,31]
    Sum = 0
    #[11,21,23,31]
    for no in Elements:
        Sum = Task(Sum,no)
    return Sum

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)

    FData=list(filterX(CheckEven , Data))               #typecasting is done to assign it as list,or else ID of FData will be displayed
    print("Data after filter is : ",FData)

    MData = list(mapX(Increment ,FData))
    print("Data after map is : ",MData)

    RData = reduceX(Add , MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()

