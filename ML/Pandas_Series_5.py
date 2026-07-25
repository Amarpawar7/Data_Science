import pandas as pd         


def main():
    sobj = pd.Series([25000,27000,29000,30000], index=["C++","C","Python","Java"])        # Strings can also be gives as index/keys

    print(sobj)

    print(sobj["Python"])   # keys can be used to access data

if __name__ == "__main__":
    main()