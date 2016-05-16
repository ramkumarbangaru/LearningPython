''' Ram's scenario:
1) Get input from User
2) Validate if it is valid numeric inputs
3) Validate if it is proper IP
4) If Valid IP then what is the class it belongs to
5) Do it using class
'''



def IsIPValid():
    ipaddr = input("Please enter the IP address: \n ")
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
