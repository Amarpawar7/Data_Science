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



if __name__ == "__main__":
    main()