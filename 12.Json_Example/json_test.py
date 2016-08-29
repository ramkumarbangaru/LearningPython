import json
f = open("C://python_test//json_test.json","r")
b=f.read()
#print (b)
c={}
c= json.loads(b)

print(c['data'][0].keys())

#print(c['data'][0]['obj_id'])
