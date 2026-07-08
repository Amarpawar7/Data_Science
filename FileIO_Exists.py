import os

def main():
    FileName = input("Enter the name of the file : ")

    Ret = os.path.exists(FileName)                              # when path start from / its absolute path ,whereas the other short path is realtive path

    if(Ret == True):
        fobj = open(FileName,"r")
        print("File gets succesfully opened")
    
    else:
        print("There is no such file")


if __name__ =="__main__":
    main()
