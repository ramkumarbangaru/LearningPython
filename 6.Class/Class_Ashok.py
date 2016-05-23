''' Ram's scenario:
1) Get input from User
2) Validate if it is valid numeric inputs
3) Validate if it is proper IP
4) If Valid IP then what is the class it belongs to
5) Do it using class
'''

ipaddr = input("Please enter the IP address: \n ")
print (ipaddr)
ip = IsIPValid(ipaddr)
print (ip.res)

def IsIPValid(object):
    """To check given IP is valid or not"""
    def __init__(self, ipaddr):
        self.ip = ipaddr
    def isvalid (self, ipaddr):
        for ip_oct in ipaddr.split("."):
            if ip_oct.isnumeric() == True:
                if int(ip_oct)>-1 and int(ip_oct)<256:
                    self.res = ("True")
                else:
                    self.res = ("False")
                    break
            else:
                self.res = ("False")
                break
    return self.res


