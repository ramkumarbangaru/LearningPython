import sys
ipaddr = str(input("Please type in the input IP Address:\n"))
flagip = 1
res = "You have entered an invalid IP Address"
for oct1 in ipaddr.split("."):
    if oct1.isnumeric():
        if int(oct1) > -1 and int(oct1) <= 255:
            #            print(oct1)
            if flagip == True:
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
                flagip = 0
        else:
            print("Wrong IP")
            sys.exit(1)

    else:
        res = "You have entered an invalid IP Address:"
        print(res)
        sys.exit(1)
print(res)