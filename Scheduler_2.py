import time
import datetime
import schedule

def fun():
    print("Inside fun at : ",datetime.datetime.now())

def main():
    print("Inside Marvellous Auutomation script at : ",datetime.datetime.now())

    schedule.every(20).seconds.de(fun)
    # Problem

if __name__ =="__main__":
    main()
