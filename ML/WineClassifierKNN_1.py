import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def WineClassifier(DataPath):
    Border = "_"*50
    #----------------------------------------------------------------------------
    # Step 1 : Load dataset from csv file
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 1 : Load dataset from csv file")
    print(Border)
    
    df = pd.read_csv(DataPath)

    print(Border)
    print("Few entries from the Datasets are : ")
    print(df.head())
    print(Border)


    #----------------------------------------------------------------------------
    # Step 2 : Clean the dataset by removing empty entries
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 2 : Clean the dataset by removing empty entries")
    print(Border)

    df.dropna(inplace = True)               # This will entire row with an empty cell
    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])
    print(Border)

    




def main():
    Border = "_"*50

    print(Border)
    print("Wine classifier using KNN")
    print(Border)

    WineClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()