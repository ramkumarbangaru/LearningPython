''' Ram's scenario:
1) Get two input
2) Give the value 0 for Denominator
3) Handle the error
4) Next step handle the other errors (Like if we give string instead of numeric)
5) How to handle unknown error with unknown resolution
'''

# Below scenario works with while loop ocndition
# import sys
# while True:
# try:
#     n = input("Numerator:")
#     d = input("Denominator:")
#     print (int(n) / int(d))
#         break
#     except ZeroDivisionError:
#         print ("Division by Zero error")
#         break
#     except ValueError:
#         print ("Only Numeric Values please")
#         break
# except:
#     print ("Unexpected error:", sys.exc_info()[0])
#         break

#Below scenario works without any loop condition
import sys
try:
    n = input("Numerator:")
    d = input("Denominator:")
    print (int(n) / int(d))
except:
    print ("Unexpected error:", sys.exc_info()[0])