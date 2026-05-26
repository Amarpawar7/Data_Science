# One function can call another function

def fun():
    print("Insidg fun")

def gun():
    print("Inside gun")
    fun()

def main():
    gun()
    
if __name__ == "__main__":
    main()

