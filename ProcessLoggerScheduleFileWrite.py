import psutil
import sys         # for command line arguments
import os             # for checking direcory path
import time                  # for time stamp
import schedule                # apply schedule for making file

def CreateLog(FolderName):
    Border = "-"*50
    Ret =  os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log files is created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")                        # strftime : used to display time in string format
    
    FileName = os.path.join(FolderName,"Demo_%s.log"%timestamp)           # used to join path
    print("Log file gets created with name ",FileName)

    fobj = open(FileName,"w")
    
    fobj.write(Border+"\n")
    fobj.write("---- Platform Surveillence System -----\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(Border+"\n")
    fobj.write("----------------- End of log file ----------------\n")
    fobj.write(Border+"\n")

def main():
    Border = "-"*50
    print(Border)
    print("---- Platform Surveillence System -----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1 : Create Automatic logs")
            print("2 : Executes Periodically")
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

        # Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog , sys.argv[2])
        
        # schedule.every(int(sys.argv[1])).seconds.do(CreateLog , sys.argv[2])

        print("Platform Surveillence System started Succesfully")
        print("Directory created with name : ",sys.argv[2])
        print("TimeInterval in minutes: ",sys.argv[1])
        print("Press CTRL + C to abort")
        
        # Wait till abort
        
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments ")
        print("Unable to proceed as there is no such option")
        print("PLease use --h or --u to get more details")


    print(Border)
    print("--------- Thank you for using my script ---------")
    print(Border)

if __name__ == "__main__":
    main()
    