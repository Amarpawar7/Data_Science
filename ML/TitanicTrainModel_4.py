import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix


#------------------------------------------------------------------------------
#  Function Name  : TrainTitanicModel()
#  Description    : Split X,Y,training data,testing data
#  Parameters     : df
#  Return         : none
#  Date           : 14/03/2026
#  Author         : Amar Dattatrya Pawar
#------------------------------------------------------------------------------


def TrainTitanicModel(df):
    # split features and labels
    X = df.drop("Survived",axis = 1)
    Y = df["Survived"]

    print("\nFratures : ")
    print(X.head())
    print("\nLabel : ")
    print(Y.head())

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train,Y_train)

    print("Model trained succesfully!")

    print("\nIntercept of model = ")
    print(model.intercept_)

    print("\nCoefficient of model ")
    for feature,coefficient in zip(X.columns, model.coef_[0]):
        print(feature, ":", coefficient)


#------------------------------------------------------------------------------
#  Function Name  : DisplayINfo()
#  Description    : It displays the formated title
#  Parameters     : title(str)
#  Return         : none
#  Date           : 14/03/2026
#  Author         : Amar Dattatrya Pawar
#------------------------------------------------------------------------------

def DisplayInfo(Title):
    print("\n" + "="*70)
    print(Title)
    print("-" * 70)


#------------------------------------------------------------------------------
#  Function Name  : ShowData()
#  Description    : It shows basi information about detaset
#  Parameters     : df
#                   df ->  Pandas dataframe object
#                   message
#                   message -> heading text to display
#  Return         : none
#  Date           : 14/03/2026
#  Author         : Amar Dattatrya Pawar
#------------------------------------------------------------------------------

def ShowData(df,message):
    DisplayInfo(message)

    print("\nFirst 5 rows of dataset")
    print(df.head())
    
    print("\nShape of dataset")
    print(df.shape)

    print("\nColumn names L ")
    print(df.columns.tolist())

    print("\nMissing values in each column")
    print(df.isnull().sum())



#------------------------------------------------------------------------------
#  Function Name  : CleanTitanicData()
#  Description    : It does preprocessing
#                 : It removes unnecessary columns
#                 : It handles missing values
#                 : It converts text Data to numeric format
#                 : It does encoding of categorical columns
#  Parameters     : df -> Pandas dataframe
#  Return         : df -> Clean Pandas dataframe
#  Date           : 14/03/2026
#  Author         : Amar Dattatrya Pawar
#------------------------------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 : Original Data")
    print(df.shape)
    print(df.head())

    # Remove unnecessary  columns
    drop_columns = ["Passengerid","zero","Name","Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\nColumns to be droped : ")
    print(existing_columns)

    # Drop the unwanted columns
    df = df.drop(columns = existing_columns)

    DisplayInfo("Step 2 : Data after column removal : ")
    print(df.shape)
    print(df.head())

    # Handle Age Column
    if "Age" in df.columns:
        print("Age columns before filling missing values")
        print(df["Age"].head(10))

        # coerce -> Invalid vlaue gets converted as NAN
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    
        age_median = df["Age"].median()

        # Replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\nAge column after perpprocessing : ")
        print(df["Age"].head(10))

    # Handle fare column
    if "Fare" in df.columns:
        print("\n Fare column before preprocessing : ")
        print(df["Fare"].head(10))
        
        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")
    
        Fare_median = df["Fare"].median()

        print("\nMedian of fare columns is: ",Fare_median)
        # Replace missing values with median
        df["Fare"] = df["Fare"].fillna(age_median)

        print("\nFare column after perpprocessing : ")
        print(df["Fare"].head(10))

    # Handle Embarked column
    if "Embarked" in df.columns:
        print("\n Embarked column before preprocessing : ")
        print(df["Embarked"].head(10))

        # Convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()          # astype -> changes in string

        # Remove missing values
        df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)

        # Get most frequent value
        embarked_mode = df["Embarked"].mode()[0]
        print("\nMode of EMbarked column : ",embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\nEmbarked column after perpprocessing : ")
        print(df["Embarked"].head(10))


    # Handle Sex column
    if "Sex" in df.columns:
        print("\n Sex column before preprocessing : ")
        print(df["Sex"].head(10))
        
        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")

        print("\nSex column after preprocessing : ")
        print(df["Sex"].head(10))



    DisplayInfo("Data after preprocessing : ")
    print(df.head(10))

    print("Missing values after preprocessing : ")
    print(df.isnull().sum())


    # Encode Embarked column
    df = pd.get_dummies(df,columns=["Embarked"],drop_first=True)      # dummies :1 hot encoding? -> 1-1 & hot -0 ......replaces variable content into no of columns 
    print("\nData after encoding")

    print(df.head())

    print("Shape of Dataset : ",df.shape)

    # Convert boolean columns into integer
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\nData after removing boolean ")

    print(df.head())


    return df   


#------------------------------------------------------------------------------
#  Function Name  : TitanicLogistic()
#  Description    : This is main pipeline controller
#                 : It shows th dataset, shows raw data
#                 : It preprocess the dataset & train the model
#  Parameters     : Data path of dataset file
#  Return         : none
#  Date           : 14/03/2026
#  Author         : Amar Dattatrya Pawar
#------------------------------------------------------------------------------

def TitanicLogistic(DataPath):
    DisplayInfo("Step 1 : Loading the dataset")  
    df = pd.read_csv(DataPath)

    ShowData(df,"Initial dataset")

    df = CleanTitanicData(df)

    TrainTitanicModel(df)


#------------------------------------------------------------------------------
#  Function Name  : main
#  Description    : Starting point of th eapplication
#  Parameters     : None
#  Return         : none
#  Date           : 14/03/2026
#  Author         : Amar Dattatrya Pawar
#------------------------------------------------------------------------------

def main():
    TitanicLogistic("MarvellousTitanicDataset.csv")



if __name__ == "__main__":
    main()