import os

def main():
    FileName = input("Enter the name of the file : ")

    Ret = os.path.isabs(FileName)                  # Absolute path

    if(Ret == True):
        print("It is absolute path")
    else:
        print("It ia relative path")


if __name__ =="__main__":
    main()
 