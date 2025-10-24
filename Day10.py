First=input("enter a 1st no = ")
opration=input("+,-,*,/, =   ")
Second=input("enter a 2nd no.= ")

First=int(First)
Second=int(Second)

if opration == "+":
    print(First+Second )

elif opration == "-":
    print(First-Second )

elif opration == "*":
    print(First*Second)

elif opration == "/":
    print(First/Second)

else :                   
    print("not validation ")