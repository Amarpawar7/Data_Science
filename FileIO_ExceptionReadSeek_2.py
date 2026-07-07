# seek(where to, form where)
# from where : 0 / 1 / 2
# 0 : Starting
# 1 : Current
# 2 : End


def main():
    try:
        fobj=open("Hello.txt","r")
        print("File gets succesfully opened")

        print("current offset is : ",fobj.tell())     # 0 offset

        fobj.seek(7,0)

        print("current offset is : ",fobj.tell())     # 7 offset

        Data = fobj.read(10)

        print("current offset is : ",fobj.tell())     # 17

        print("Data from file is : ",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")
    
    finally:
        print("End of application")

if __name__ =="__main__":
    main()
 
