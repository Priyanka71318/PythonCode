



class school ():
    def name(self):
        print("ABC school")
class student(school):
    def study(self):
        print("Student is studying")
s11=school()
s12=student()
s11.name()
s12.study()

print(student.mro())

