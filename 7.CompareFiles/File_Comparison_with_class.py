import os
os.chdir("C:/python_test/")
class compare():
    def readfile(self,file1,file2):
        d = open(file1,"r")
        e = open(file2,"r")
        list1 = d.readlines()
        list2 = e.readlines()
        self.list1 = list1
        self.list2 = list2
        return(list1,list2)

    def matchfile(self,list1,list2):
        # list1 = file1.readlines()
        # list2 = file2.readlines()
        if (list1==list2):
            print("MATCH")
        else:
            print("MISSMATCH")

a = str(input("Enter file1:\n"))
b = str(input("Enter file2:\n"))
print(os.getcwd())
c = compare()
c.readfile(a,b)
print(c.list1,c.list2)
c.matchfile(c.list1,c.list2)