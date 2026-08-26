import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error,r2_score


#----------------------------------------------------------------------------
# Step 1 : Load dataset
#----------------------------------------------------------------------------
Border = "-"*50
print(Border)
print("Step 1 : Load dataset")
print(Border)

df = pd.read_csv("california_housing.csv")
print("Shape of dataset : ",df.shape)
print("First 5 records : ",df.head())


#----------------------------------------------------------------------------
# Step 2 : Seperate features and labels
#----------------------------------------------------------------------------

X = df.drop("target",axis= 1)
Y = df["target"]


#----------------------------------------------------------------------------
# Step 3 : Split dataset for training and testing
#----------------------------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


#----------------------------------------------------------------------------
# Step 4 : Create the Base model
#----------------------------------------------------------------------------

base_model = DecisionTreeRegressor(random_state=42)


#----------------------------------------------------------------------------
# Step 5 : Create Bagging model
#----------------------------------------------------------------------------

bagging_model = BaggingRegressor(
    estimator = base_model,
    n_estimators=10,
    random_state=42
)


#----------------------------------------------------------------------------
# Step 6 : Train Bagging model
#----------------------------------------------------------------------------

bagging_model.fit(X_train,Y_train)


#----------------------------------------------------------------------------
# Step 7 : Testing bagging model
#----------------------------------------------------------------------------

Y_pred = bagging_model.predict(X_test)


#----------------------------------------------------------------------------
# Step 8 : Evaluate Bagging model
#----------------------------------------------------------------------------
# lower the mean squared error better the model
print("MeanSquaredError : ",mean_squared_error(Y_test,Y_pred))


print("R Square : ",r2_score(Y_test, Y_pred))


