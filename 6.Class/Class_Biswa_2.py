class student:
    def std(self,name,age):
        self.name = name
        self.age=age
        print ("The student name is",name,"And the age of the student is:",age)
    def stdsex(self,sex):
        self.sex=sex
        print("THe student is a",sex,"student")

std1 = student()
n = str(input("Enter the student Name:"))
a = int(input("Enter the age of the student:"))
s = str(input("Enter the sex of the student:"))
std1.std(n,a)
std1.stdsex(s)




