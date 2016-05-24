class ipc:
    #First Function Starts from Here
    def isclass(self,ipaddr):
        self.ipaddr = ipaddr
        oct1 = ipaddr.split(".")[0]
        if int(oct1) > 1 and int(oct1) < 128:
            res = "You have entered a class A IP Address:"+ipaddr
        #            print(res)
        elif int(oct1) >= 128 and int(oct1) < 192:
            res = "You have entered a class B IP Address:"+ipaddr
        #            print(res)
        elif int(oct1) >= 192 and int(oct1) < 223:
            res = "You have entered a class C IP Address:"+ipaddr
        #            print(res)
        elif int(oct1) >= 224 and int(oct1) < 240:
            res = "You have entered a class D IP Address:"+ipaddr
        #            print(res)
        elif int(oct1) >= 240 and int(oct1) < 256:
            res = "You have entered a class E IP Address:"+ipaddr
        #            print(res)
        return(res)

    # Second Function Starts from Here'''
    def isvalid(self,ipaddr):
        self.ipaddr = ipaddr
        for oct in ipaddr.split("."):
            if oct.isnumeric():
                if int(oct) > -1 and int(oct) <= 255:
                    op = "Valid IP"
                else:
                    op = "Invalid IP"
                    break
            else:
                op = "Invalid IP"
                break
        return(op)

ip = ipc()
a = str(input("Please Enter the IP Address:\n"))
if (ip.isvalid(a) == "Valid IP"):
    print(ip.isclass(a))
else:
    print("You have Entered Invalid IP")
