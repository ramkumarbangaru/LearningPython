import json
f = open("C://python_test//json_test.json","r")
b=f.read()
print (b)

c= json.loads(b)
print(c)
