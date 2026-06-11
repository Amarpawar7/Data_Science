import os

def main():
    print("PID of running process is : ",os.getpid())
    print("PID of parent process is : ",os.getppid())             # Its same whenever we run it
    

if __name__ == "__main__":
    main()
    
 