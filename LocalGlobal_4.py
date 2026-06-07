No = 11                                                  # Global Variable

def Fun():
    global No                                            #
    print("Value of No from Fun is : ",No)        # 11
    No = No + 1                                   # 12
    print("Value of No from Fun is : ",No)        # 12

print("Value of No is : ",No)              # 11
Fun()
print("Value of No is : ",No)              # 12

