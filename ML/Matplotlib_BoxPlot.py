import matplotlib.pyplot as plt
import seaborn as sns
def main():

    # Used to detect Outliers
    sns.boxplot(x = [10,20,30,110])              # used to detect outliers
    # eg : sns.boxplot(x = [2,50,60,70,500])              # used to detect outliers

    plt.show()


if __name__ == "__main__":
    main()

