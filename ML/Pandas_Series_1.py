import pandas as pd         # as is alias


def main():
    Data = [11,21,51,101,111] 

    print(Data)

    sobj = pd.Series(Data)         # sobj is object of Series , .series convers list into series , Series should contain homogeneous data

    print(sobj)

if __name__ == "__main__":
    main()