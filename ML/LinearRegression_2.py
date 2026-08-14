import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def Predictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent variables : X - ",X)
    print("Values of Dependent variables : Y - ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    
    print("X_Mean is : ",mean_x)
    print("Y_Mean is : ",mean_y)

    n = len(X)   # 5

    # Y = mX + C

    # m = (summ (X-X_bar) * (Y-Y_bar)) / summ(X-X_bar) ** 2

    numerator = 0
    denominator = 0

    for i in range (n):
        numerator = numerator + ((X[i] - mean_x)*(Y[i] - mean_y))
        denominator =  denominator + ((X[i] - mean_x) ** 2)
        
    m = numerator / denominator
    print("Slope of line i.e. m : ",m)


    c = mean_y - (m * mean_x)
    print("Y intercept of line i.e. C : ",c)

    

def main(): 
    Predictor()    



if __name__ == "__main__":
    main()
