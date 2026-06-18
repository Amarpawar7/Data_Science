# python  CommandLine_4.py  10 21
# pypi.org contains all the modules

import sys

def main():
    if(len(sys.argv) < 3 or len(sys.argv) > 3):
        print("Invalid number of argument")

    else:
        No1 = int(sys.argv[1])
        No2 = int(sys.argv[2])
        print(No1 + No2)
    
if __name__ == "__main__":
    main()

