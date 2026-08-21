import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler                           # 

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

    

    #----------------------------------------------------------------------------
    # Step 3. Seperate independent and dependent variables
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 3. Seperate independent and dependent variables")
    print(Border)

    X = df.drop(columns='Class')
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input columns : ",X.columns.tolist())
    print("Output columns : Class")



    #----------------------------------------------------------------------------
    # Step 4 : Split the dataset for training and testing
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 4 : Split the dataset for training and testing")
    print(Border)

    X_train, X_test , Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(Border)
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)
    print(Border)



    #----------------------------------------------------------------------------
    # Step 5 : Feature Scaling
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    scalar = StandardScaler()            # if stratify is Y(yes) then if we split dataset after shuffling dataset we will be recieving everytime will always be fixed,usually used in multiclass classification
    # Independent variable scaling
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feature Scaling is done")



    #----------------------------------------------------------------------------
    # Step 6 : Exlpore the multiple values of k
    # Hyperparameter tuning (K)
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 6 : Exlpore the multiple values of k")
    print(Border)

    accuracy_scores = []             # values for each k values are stored in this list
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy report of all K values from 1 to 20")
    for value in accuracy_scores:
        print(value)
    print(Border)

    

    #----------------------------------------------------------------------------
    # Step 7 : Plot graph of K vs Accuracy
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 7 : Plot graph of K vs Accuracy")
    print(Border)
    
    plt.figure(figsize=(8,5))
    plt.plot(K_values, accuracy_scores, marker= 'o')
    plt.title("K values vs Accuracy")
    plt.xlabel("value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()



    #----------------------------------------------------------------------------
    # Step 8 : Find best value oj k
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 8 : Find best value oj k")
    print(Border)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of K is : ",best_k)



    #----------------------------------------------------------------------------
    # Step 9 : Build final model using best value of k
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 9 : Build final model using best value of k")
    print(Border)

    final_model = KNeighborsClassifier(n_neighbors= best_k)
    final_model.fit(X_train_scaled,Y_train)
    final_model.predict(X_test_scaled)

    

    #----------------------------------------------------------------------------
    # Step 10 : Calculating final Accuracy
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 10 : Calculating final Accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of the model is : ",accuracy)


    
    #----------------------------------------------------------------------------
    # Step 11 : Display Confusion matrix
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 11 : Display Confusion matrix")
    print(Border)

    cm = confusion_matrix(Y_test,Y_pred)
    print(cm)



    #----------------------------------------------------------------------------
    # Step 12 : Display Classification Report
    #----------------------------------------------------------------------------
    print(Border)
    print("Step 12 : Display Classification Report")                      # due to stratify support in classification reoprt remains constant no matte rhow many times we run the program
    print(Border)

    print(classification_report(Y_test,Y_pred))
    
    


def main():
    Border = "_"*50

    print(Border)
    print("Wine classifier using KNN")
    print(Border)

    WineClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()