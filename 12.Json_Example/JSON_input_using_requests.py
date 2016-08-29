import requests
r = requests.get('https://api.github.com/user', verify=False, auth=('user', 'pass'))
#r = requests.get("http://systadash.eng.idirect.net:8080/view/CI%20Test%20suite/job/Evo-develop-8350-DLC-CarrierSanity/api/json")
#"http://systadash.eng.idirect.net:8080/view/CI%20Test%20suite/job/Evo-develop-8350-DLC-CarrierSanity/346/api/json"

#print(r.status_code)
#print(r.headers['content-type'])
#print(r.encoding)
#print(r.text)
print(r.json())
