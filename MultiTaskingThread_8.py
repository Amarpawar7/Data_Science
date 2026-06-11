import threading 

def Display(No):
    print("Inside Display : ",No)

    

def main():
    t = threading.Thread(target= Display , args=(11,    ))           # args is a tuple, args takes 11 wth it to Display function 
    t.start()
    t.join()


if __name__ == "__main__":
    main()
    