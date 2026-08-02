import pandas as pd         


def main():
    
    Data = {
        "Name" : ["Sager","Amit","Pooja"],
        "Age" : [23,26,25],
        "City" : ["Pune","Mumbai","Satara"]

    }

    dobj = pd.DataFrame(Data)

    # Feteches specific row
    print(dobj.loc[1])        # loc is lock and iloc is ilock


if __name__ == "__main__":
    main()
