import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree            # trining model and data for diaplaying it graphically

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*100



#############################################################################################
# Step 1 : Load the Dateset
#############################################################################################
print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DatasetPath = "iris.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")
print("Initial entries from dataset : ")
print(df.head())                                      # displays 5 rows form start



#############################################################################################
# Step 2 : Data Analysis(EDA(Exploratory data analysis))
#############################################################################################
print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset",df.shape) # shows no. of rows and columns
print("Column names : ",list(df.columns))

print("Missing values (per column)")
print(df.isnull().sum())

print("Class Distribution (Species Count)")
print(df["species"].value_counts())                   # count of each label

print("Statistical report of dataset")
print(df.describe())                          # count,mean,std,min,max



#############################################################################################
# Step 3 : Decide Independent and Dependent Variable
#############################################################################################
print(Border)
print("Step 3 : Decide Independent and Dependent Variable")
print(Border)

# X : Indepandent Variables / Features
# Y : Dependent Variables / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)
