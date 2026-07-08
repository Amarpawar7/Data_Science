import os

def main():
    FileName = input("Enter the name of the file : ")

    if (os.path.exists(FileName)):
        Ret = os.path.isabs(FileName)                  # isabs = Absolute path , its a blind function coz even if file doesn't exist it assigne path

        if(Ret == True):
            print("It is Absolute Path")
        else:
            print("It ia Relative Path")
            NewPath = os.path.abspath(FileName)
            print("Updated Path : ",NewPath)
    else:
        print("There is no such file")
        
if __name__ =="__main__":
    main()
