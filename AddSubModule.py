PI = 3.14
print("Inside Module : ",__name__)

def Add(No1,No2):
    Ans=0
    Ans = No1 + No2
    return Ans

def Sub(No1,No2):
    Ans=0
    Ans = No1 - No2
    return Ans

def Summation(Arr):                               #Parameterr can be either list / tuple
    sum=0

    for i in range(len(Arr)):
        sum = sum + Arr[i]
    return sum