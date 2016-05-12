# a = input("Please type the input number 1:\n")
# b = input("Please type the input number 2:\n")
#
# c = int(a)/int(b)
# print(c)

a = input("Please type the input number 1:\n")
b = input("Please type the input number 2:\n")
a = int(a)
b = int(b)
while True:
    try:
        print (a/b)
        break
    except ZeroDivisionError:
        print ("Cannot divide by zero")
        break