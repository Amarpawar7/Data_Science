Addition = lambda a,b : a+b                        # no parenthesis in lambda function

Substraction = lambda a,b : a-b

No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

Ans = Addition(No1,No2)                          # Ans = No1 + No2        -> Ans = 11 + 10
print("Addition is : ",Ans)

Ans = Substraction(No1,No2)                      # Ans = No1 - No2        -> Ans = 11 - 10
print("Substraction is : ",Ans)

