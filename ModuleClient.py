import AddSubModule

print("Inside Client : ",__name__)
print("Value of PI is : ",AddSubModule.PI)

Result = 0

Result = AddSubModule.Add(20,10)
print("Addition is : ",Result)

Result = AddSubModule.Sub(20,10)
print("Substraction is : ",Result)
