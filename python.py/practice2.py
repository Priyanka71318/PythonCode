   #Practice classes, objects and constructors   

class empolyer :
   Name = "Priyanka pagare "
   salary = 50

s1=empolyer()  
print( "Name:",s1.Name)
print("salary:",s1.salary)

class car:
   brand ="mahindra"
   colour="red"
s2=car()
print("Brands:",s2.brand)
print("colour:",s2.colour)

class student:
   def __init__(self,Name,Marks):
      self.Namestu =Name
      self.Marksstu=Marks
s3=student("Priyanka",100)
print("Name:",s3.Namestu)
print("marks:",s3.Marksstu)

s5=student("Raj jain",50)
print("Name:",s5.Namestu)
print("marks:",s5.Marksstu)

class moblie:
   def __init__(self,model,price):
      self.model=model
      self.price=price
s4=moblie("motorola",25000)
print("MODEL:-",s4.model)
print("price:-",s4.price)

