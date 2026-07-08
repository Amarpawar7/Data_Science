import os

def main():
    FileName = input("Enter the name of the file : ")   # Demo.txt

    if (os.path.exists(FileName)):
        fobj = open(FileName,"w")
 
        print(fobj.readable())         # True is open in read mode or else false
        print(fobj.writable())         # True is open in write mode or else false
        print(fobj.seekable())         # False
        
    else:
        print("There is no such file")
        
if __name__ =="__main__":
    main()
    