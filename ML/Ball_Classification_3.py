from sklearn import tree

# following is one hot encoding
# Rough = 1
# Smooth = 0

# Tennis = 1
# Cricket = 2

def main():
    print("Ball Classification Case Study")

    # Data Loading / Gathering

    # Independent Variables
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 

    # Dependent Variables
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # model Selection
    modelobj = tree.DecisionTreeClassifier()
    
    # training
    trainedmodel = modelobj.fit(Features , Labels)

    # testing
    Result = trainedmodel.predict([[37,1],[94,0]])     # output : [1 2]

    print("Model Predictes the object as : ",Result)



if __name__ == "__main__":
    main()
 
# Dataset Size : 15
