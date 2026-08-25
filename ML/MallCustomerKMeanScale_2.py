import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans




def main():
    Border = "_"*50
    #----------------------------------------------------------------------------
    # Step 1 : Load dataset from csv file
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 1 : Load dataset from csv file")
    print(Border)

    df = pd.read_csv("Mall_Customers.csv")

    print("First few records : ")
    print(df.head())

    print("Shape of dataset : ",df.shape,"\n")

    print("Missing values : ")
    print(df.isnull().sum())


    #----------------------------------------------------------------------------
    # Step 2 : Select features
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 2 : Select features")
    print(Border)

    X = df[["AnnualIncome", "SpendingScore"]]
    print("Selected features : ")
    print(X.head())

    print("Shape of selected features is : ",df.shape)


    #----------------------------------------------------------------------------
    # Step 3 : Scale the data
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 3 : Scale the data")
    print(Border)

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("Data after Scalling : ")
    print(X_scaled[:5])




if __name__ == "__main__":
    main()