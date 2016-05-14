''' Ram's scenario:
1) Get input from User
2) Validate if it is valid numeric inputs
3) Validate if it is proper IP
4) If Valid IP then what is the class it belongs to
5) Do it using function
'''

def IsIPValid(ipaddr):
    "This function will validate the given input is valid IP or Not"
    for ip_oct in ipaddr.split("."):
        if ip_oct.isnumeric() == True:
            if int(ip_oct)>-1 and int(ip_oct)<256:
                res = ("True")
            else:
                res = ("False")
                break
        else:
            res = ("False")
            break
    return (res)

def IPClass(ipaddr):
    "This function will validate the given input is valid IP or Not"
    octets = ipaddr.split(".")
    if octets[0].isnumeric() == True:
        if int(octets[0])>-1 and int(octets[0])<128:
            res = ("Given IP belongs to class A")
        elif int(octets[0])>127 and int(octets[0])<192:
            res = ("Given IP belongs to class B")
        elif int(octets[0])>191 and int(octets[0])<224:
            res = ("Given IP belongs to class C")
        elif int(octets[0])>223 and int(octets[0])<240:
            res = ("Given IP belongs to class D")
        elif int(octets[0])>239 and int(octets[0])<256:
            res = ("Given IP belongs to class E")
        else:
            res = ("Not a valid IP Class")
    else:
        res = ("Not a Valid Input")
    return (res)

#This is the Main Program
ipaddr = input("Please enter the IP address: \n ")
if (IsIPValid(ipaddr)) == "True":
    res = (IPClass(ipaddr))
else:
    res = ("Not a valid IP")
print (res)

