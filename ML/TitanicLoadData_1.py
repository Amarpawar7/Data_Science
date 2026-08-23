import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix


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