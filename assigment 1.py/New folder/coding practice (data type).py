"""# converted decimal to hexadecimal26
num=int(input("enter a decimal number:- "))
hexa=hex(num)[2:] # [2:] is a inindex 2 se stard to ending index
print("Hexadecimal:-",hexa)

#  converted hexadecimal to decimal
hexa=input("enter a hexademila number")
decimal=int(hexa)[2:]
print("Decimal:-",decimal)

# Type checker
a = int(input("enter a number"))
print(type(a))

b = float(input("enter a number"))
print(type(b))

c = input("enter a charcter")
print(type(c))

d = input("enter a boolen value ")
print(type(d))"""

num = int(input("Enter a number: "))

# Positive, Negative ya Zero
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# Even ya Odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")







