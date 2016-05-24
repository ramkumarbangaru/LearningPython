''' Ram's scenario:
1) Get input from User
2) Validate if it is valid numeric inputs
3) Validate if it is proper IP
4) If Valid IP then what is the class it belongs to
5) Do it using class
'''

class IPValidation:
    """To check given IP is valid or not"""
    def isvalid (self, ipaddr):
        self.ipaddr = ipaddr
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
    def IPClass(self, ipaddr):
        octets = ipaddr.split(".")
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
        return (res)

ipaddr = input("Please enter the IP address: \n ")
#print (ipaddr)
ip = IPValidation()
if (ip.isvalid(ipaddr) == "True"):
    print (ip.IPClass(ipaddr))
else:
    print ("Not a valid IP")
