# Accept : Multiple Parameters
# Return : One Value
def Demo(Value1,Value2):
    print("Inside demo : ",Value1, Value2)
    return 11

def main():
    Result = None 
    Result = Demo("Python", 21)
    print("Return Value is : ",Result)

if __name__ == "__main__":
    main()

