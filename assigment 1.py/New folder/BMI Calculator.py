weight = int(input("enter your weight :- "))
height= float(input("enter you height :- "))
height=height*0.3048#feet to meter
BMI=weight/(height*height)
print("BMI =",round(BMI,2))
if BMI<18.5:
    print("underweight")
elif BMI<25:
    print("normal weight")
elif BMI<30:
    print("Overweight ")
else :
    print("obese")

