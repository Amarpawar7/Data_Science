# X                 Y               Result
# -----------------------------------------
# 1                 2                 * (Red)
# 2                 3                 * (Red)
# 3                 1                 . (Blue)
# 5                 6                 . (Blue)
# -----------------------------------------

# [A,B,C,D]
#X[1,2,3,5]
#Y[2,3,1,6]
# [R,R,B,B]

# Predict(3,3) -> ?


def KNeighbourClassifier():
    border = "-"*50
    data = [
                {'point' : 'A', "X" : 1, 'Y' : 2, 'label' : 'Red'},
                {'point' : 'A', "X" : 2, 'Y' : 3, 'label' : 'Red'},
                {'point' : 'A', "X" : 3, 'Y' : 1, 'label' : 'Blue'},
                {'point' : 'A', "X" : 5, 'Y' : 6, 'label' : 'Blue'},                  
            ]

    print(border)
    print("User Defined KNN")
    print(border)


    print(border)
    print("Training Dataset")
    print(border)

    for i in data:
        print(i)

    print(border)




def main():

    KNeighbourClassifier()
    

if __name__ == "__main__":
    main()