'''
This program is for regular expression which consider one/multiple same letter as one letter for matching
'''

import re


s=input("Please write the string with duplicate charcters:")
print(type(s))
if s == str:
    a = re.compile(r'(([a-z])\2{1,})',re.I)
    r= a.sub(r'\2',s)
    print(r)

    # r= re.sub(r'(([a-z])\2{1,})',r'\2',s)

    ''''
    a = re.compile(r'([a-z])\1+',re.I)
    r = a.sub(r'\1', s)
    print(r)
    '''
else:
    print("Invalid string:")



