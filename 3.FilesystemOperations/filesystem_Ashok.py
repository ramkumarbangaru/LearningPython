''' Ram's scenario:
1) Change the default directory. Hard code now later get it from user
2) Read the files, directories from the given directory
3) Get input from User for file extension like (txt, iso, .xlsx, .doc etc..)
4) Print the count of files with provided file extension
5) Run it in windows and Linux machine
'''

import os
#print(os.getcwd())
#os.chdir("C:/Ashok/Test")
#print(os.getcwd())
file_extenstion =input("Please Enter the file Extension: \n")
count = 0
for root, dirs, files in os.walk("C:\Ashok\Test"):
    for name in files:
        #print(os.path.join(root, name))
        if file_extenstion == name.split(".")[-1]:
            count = count+1
print (count)
