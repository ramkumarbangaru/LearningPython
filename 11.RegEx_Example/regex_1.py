import re
print("Enter the number please:")
a=input()
# b= re.match(r'-\d{2}.\d{2}',a)
b= re.match(r'^-[3][5].[5-9]|^-3[6-9].[0-9]|^-[4-5][0-9].[0-9]|^-6[0-4].[0-9]|^-6[5].[0-5]',a)

print(b)