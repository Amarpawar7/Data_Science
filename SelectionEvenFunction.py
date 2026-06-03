def CheckEven(num):
    if(num%2 == 0):
        print("It is Even.")
    else:
        print("It is Odd")


def main():
    CheckEven(21)           #Positional
    CheckEven(num = 22)     #Keyword

if __name__ == "__main__":
    main()
