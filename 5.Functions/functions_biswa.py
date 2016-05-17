import sys
ipaddr = str(input("Please type in the input IP Address:\n"))
res = "You have entered an invalid IP Address"
ip = "You have entered an valid IP Address"
ip1 = "You have entered an invalid IP Address"
def ipvalid(ipaddr):
    for oct in ipaddr.split("."):
        if oct.isnumeric():
            if int(oct) > -1 and int(oct) <= 255:
                op = ip
            else:
                op = ip1
                break
        else:
            op = ip1
            break
    return(op)
def ipclass(ipaddr):
    oct1 = ipaddr.split(".")[0]
    if int(oct1) > 1 and int(oct1) < 128:
        res = "You have entered a class A IP Address:"+ipaddr
    elif int(oct1) >= 128 and int(oct1) < 192:
        res = "You have entered a class B IP Address:"+ipaddr
    elif int(oct1) >= 192 and int(oct1) < 223:
        res = "You have entered a class C IP Address:"+ipaddr
    elif int(oct1) >= 224 and int(oct1) < 240:
        res = "You have entered a class D IP Address:"+ipaddr
    elif int(oct1) >= 240 and int(oct1) < 256:
        res = "You have entered a class E IP Address:"+ipaddr
    return(res)


if ipvalid(ipaddr) == ip:
    ipclass(ipaddr)
else:
    print(ip1)
sys.exit(1)