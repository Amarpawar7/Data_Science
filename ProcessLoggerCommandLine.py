# This code is for taking Command line inputs 

import psutil
import sys         # for command line arguments

def main():
    Border = "-"*50
    print(Border)
    print("---- Platform Surveillence System -----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("THis script is used to : ")
            print("1 : Create Automatic logs")
            print("2 : Executes Preiodically")
            print("3 : Send mail with logs")
            print("4 : Store information about processess")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secondary storage i.e. harddisk")


        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):    
            print("Use the automation script as : ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of Directory to create auto log")

        else : 
            print("Unable to proceed as there is no such option")
            print("PLease use --h or --u to get more details")

    # python Demo.py 5 Demo
    elif(len(sys.argv) == 3):
        print("Inside Project's logic")
        print("TimeInterval : ",sys.argv[1])
        print("DirectoryName : ",sys.argv[2])


    else:
        print("Invalid number of command line arguments ")
        print("Unable to proceed as there is no such option")
        print("PLease use --h or --u to get more details")


    print(Border)
    print("--------- Thank you for using my script ---------")
    print(Border)

if __name__ == "__main__":
    main()