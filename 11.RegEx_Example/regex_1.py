import re
# print("Enter the number please:")
# a=input()
# # b= re.match(r'-\d{2}.\d{2}',a)
# b= re.match(r'^-[3][5].[5-9]|^-3[6-9].[0-9]|^-[4-5][0-9].[0-9]|^-6[0-4].[0-9]|^-6[5].[0-5]',a)
#
# print(b)

c = re.match("(\w{3})\d{2}(\w{4})","Ram20abcd")
print(c.group(0))
print(c.group(1))
print(c.group(2))