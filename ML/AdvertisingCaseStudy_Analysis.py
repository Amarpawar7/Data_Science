import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score


def Advertise(Datapath):
    Border = "_"*50
    #----------------------------------------------------------------------------
    # Step 1 : Load dataset
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 1 : Load dataset")
    print(Border)

    df = pd.read_csv(Datapath)
    Border = "_"*50
    print("few records from datasets : ")
    print(df.head())


    #----------------------------------------------------------------------------
    # Step 2 : Remove unwanted columns
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 2 : Remove unwanted columns")
    print(Border)

    print("Shape of dataset before removel : ",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape of dataset after removel : ",df.shape)

    print(Border)
    print("Clean dataset is :")
    print(Border)

    print(df.head())



    #----------------------------------------------------------------------------
    # Step 3 : Chack missing values
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 3 : Chack missing values")
    print(Border)

    print("Missing values count : \n",df.isnull().sum())


    #----------------------------------------------------------------------------
    # Step 4 : Display Stastical Summary
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 4 : Display Stastical Summary")
    print(Border)

    print(df.describe())


    #----------------------------------------------------------------------------
    # Step 5 : Correlation between columns
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 5 : Correlation between columns")
    print(Border)
    
    print("Correlation Matrix")
    print(df.corr())






def main():
        
    Advertise("Advertising.csv")
    



if __name__ == "__main__":
    main()