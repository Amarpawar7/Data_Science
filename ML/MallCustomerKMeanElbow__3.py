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


    #----------------------------------------------------------------------------
    # Step 4 : Use Elbow method
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 4 : Use Elbow method")
    print(Border)
    
    WCSS = []

    for i in range(1,11):
        model = KMeans(n_clusters=i, random_state=42, n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11), WCSS, marker = 'o') # small o
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow method")
    plt.grid(True)
    plt.show()    
    # k = 4

    #----------------------------------------------------------------------------
    # Step 5 : Train the model
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 5 : Train the model")
    print(Border)
    
    model = KMeans(n_clusters=4, random_state=42, n_init=10)
    clusters = model.fit_predict(X_scaled)

    df["clusters"] = clusters

    print("Dataset with clusters")
    print(df.head(30))




if __name__ == "__main__":
    main()