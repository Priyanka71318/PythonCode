         # inheritance practice
class Animal :
    def eat(self):
        print("eating")
class Dog (Animal):
    def bark(self):
        print("barking")
s1 = Dog()
s1.eat()
s1.bark()

             # polymorphism practice
  #Write a Python program to demonstrate polymorphism using two classes UPI and Card
class UPI:
    def pay(self):
        print("payment through UPI")
class card:
    def pay(self):
        print("payment through card")
s1=UPI()
s2=card()

s1.pay()
s2.pay()

# Write a Python program to demonstrate polymorphism using two classes Car and Bike.
class car :
    def star(self):
        print("car stars")
class bike :
    def star(self):
        print("bike stars")
c1=car()
b1=bike()

c1.star()
b1.star()
# Problem 3 — Notification 📱
class SMS:
    def send(self):
        print("Sending message via SMS")
class Whatsapp:
    def send(self):
        print("sending message via whatsapp")
class Email:
    def send(self):
        print("sending message via Email")
cl1=SMS()
cl2=Whatsapp()
cl3=Email()

cl1.send()
cl2.send()
cl3.send()