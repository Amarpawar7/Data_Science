import pandas as pd         


def main():
    
    # 
    Data = {
        "Name" : ["Sager","Amit","Pooja"],
        "Age" : [23,26,25],
        "City" : ["Pune","Mumbai","Satara"]

    }

    dobj = pd.DataFrame(Data)

    print(dobj)

    
    # sobj = pd.DataFrame([25000,27000,29000,30000], index=["blue","red","green","yellow"])     

    # print(sobj)


if __name__ == "__main__":
    main()
