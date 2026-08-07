import matplotlib.pyplot as plt
import seaborn as sns

def main():

    # Categorical Data
    sns.countplot(x = ["A","B","A","A","B","A","C"])      # if categorical data

    plt.show()


if __name__ == "__main__":
    main()