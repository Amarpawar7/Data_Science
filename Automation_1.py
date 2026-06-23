import sys

def main():
    Border = "_"*40
    print(Border)
    print("--------- Automation --------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform __________")
            print("This is an automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py Argument1 Argiment2")
            print("Argument1 : ________________")
            print("Argument2 : ________________")

        else:
            print("Use the given flags as : ")
            print("--u : Used to display usage")
            print("--h : Used to display help")
    else:
        print("Invalid number of commandline arguments")
        print("Use the given flags as : ")
        print("--u : Used to display usage")
        print("--h : Used to display help")

    print(Border)
    print("----Thank you for using our script -----")
    print("-------- Infosystems --------")
    print(Border)

if __name__ == "__main__":
    main()