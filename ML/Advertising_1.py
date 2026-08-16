import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def main():
    Border = "-"*50
    print(Border)

    df = pd.read_csv("Advertising.csv")
    print("dataset before droping unnamed column",df.shape)                     # ( 200, 5)
    
    # Data cleaning

    if 'Unnamed: 0' in df.columns:               # it removes unnamed column
        df.drop(columns=['Unnamed: 0'], inplace= True)

    print("dataset after droping unnamed column",df.shape)



if __name__ == "__main__":
    main()