def Demo():
    print("Inside Demo")

    def hello():
        print("Inside hello")

def main():
    Demo.hello()    #Error
    
    
if __name__ == "__main__":
    main()

