import sys       # for command line arguments
import os
def DirectoryScanner(DirName = "Demo"):
    Ret = False

    Ret = os.path.exists(DirName)

    if (Ret == False):
        print("There is no such directory ")
        return

    Ret = os.path.isdir(DirName)

    if (Ret == False):
        print("It is not a directory")
        return 
    
    for FolderName , SubName , FileName in os.walk (DirName):
        for fname in FileName:                                        # Shows all the files including the file inside subfolders
            print("File Name : ",fname)
            print("File size : ",os.path.getsize(fname))                   # ERROR : Path issue

        
def main():
    Border = "_"*50
    print(Border)
    print("---------Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of Directory")
        return
    
    DirectoryScanner(sys.argv[1])


if __name__ == "__main__":
    main()