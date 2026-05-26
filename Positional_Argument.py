def Display(A,B,C,D):
    print(A,B,C,D)

def main():
    #Display(10,20)             #Not allowed : Less Arguments ____________TypeError: Display() missing 2 required positional arguments: 'C' and 'D'
    #Display(10,20,30,40,50)              #no allowed : Extra Arguments _________________TypeError: Display() takes 4 positional arguments but 5 were given
    Display(10,20,30,40)                  #ALLOWED

if __name__ == "__main__":
    main()