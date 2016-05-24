import os
os.chdir("C:\\python_test\\")
print(os.getcwd())

file1 = open("a.txt", "r")
list1 = file1.readlines()
file2 = open("b.txt", "r")
list2 = file2.readlines()

if(list1==list2):
    print("Both File Maches")
else:
    print("Not Matching")
