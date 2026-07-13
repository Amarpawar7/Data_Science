import psutil
import sys         # for command line arguments
import os             # for checking direcory path
import time                  # for time stamp
import schedule                # applu=y schedule for making file

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
    
    FileName = os.path.join(FolderName,"Demo_%s.log"%timestamp)          # used to join path
    print("Log file gets created with name ",FileName)

    fobj = open(FileName,"w")
    
    fobj.write(Border+"\n")
    fobj.write("---- Platform Surveillence System -----\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------------- System Report -----------------\n")





    # print("CPU Usage : ",psutil.cpu_percent())
    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())

    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    # print("RAM usage : ",mem.percent)
    fobj.write("RAM usage : %s %%\n" %mem.percent)

    fobj.write(Border+"\n")

    fobj.write("\nDisk Usage Report\n")
    for part in psutil.disk_partitions():
        try:  
            usage = psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent))
        except:
            pass

    fobj.write(Border+"\n")

    net = psutil.net_io_counters()                               # report about how much date is sent via internet
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024*1024)))             # %2f : 2 digits after decimal
    fobj.write("Recived : %.2f MB\n" % (net.bytes_recv / (1024*1024))) 

    fobj.write(Border+"\n")




    # Process Log 

    fobj.write(Border+"\n")
    fobj.write("----------------- End of log file ----------------\n")
    fobj.write(Border+"\n")
 
    
def ProcessScan():
    print("Process Scan Report")

    for proc in psutil.process_iter(attrs=["pid", "name", "status"]):
        info = proc.info
        print(info["pid"], info["name"], info["status"])

def main():
    ProcessScan()

    return

    Border = "-"*50
    print(Border)
    print("---- Platform Surveillence System -----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
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
    