import pandas as pd         


def main():
    sobj = pd.Series([11.0,21.0,51.0,101.0,111.0])        # python doesn't consider datatype but pandas do consider datatypes

    print(sobj)

if __name__ == "__main__":
    main()