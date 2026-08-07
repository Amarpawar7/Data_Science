import matplotlib.pyplot as plt
import seaborn as sns

def main():

    # Contiguous Values 
    sns.histplot(data = [10,20,30,20,20,20,30,40])         # if we pass independent variables like sepal& petals width and lenth

    plt.show()


if __name__ == "__main__":
    main()