''' Ram scenario Two:
1) Get input from User
2) Validate if it is valid numeric inputs
3) Validate if it is proper IP
2) If Valid IP then what is the class it belongs to
'''

#print ("This script will validate the given input is valid IP or Not and the class of IP if it is valid IP")
ip_input = input("Please enter the IP address: \n ")
foct = "true"
for ip_oct in ip_input.split("."):
    if ip_oct.isnumeric() == True:
        if foct is 'true':
            if int(ip_oct)>0 and int(ip_oct)<128:
                res = ("Given IP belongs to class A")
            elif int(ip_oct)>127 and int(ip_oct)<192:
                res = ("Given IP belongs to class B")
            elif int(ip_oct)>191 and int(ip_oct)<224:
                res = ("Given IP belongs to class C")
            elif int(ip_oct)>223 and int(ip_oct)<240:
                res = ("Given IP belongs to class D")
            elif int(ip_oct)>239 and int(ip_oct)<256:
                res = ("Given IP belongs to class E")
            else:
                res = ("Not a valid IP")
            foct = "false"
        else:
            if int(ip_oct) < 0 or int(ip_oct) > 255:
                res = ("Not a valid IP")
    else:
        res = ("Given input is not a numeric input for Valid IP " +ip_input)
print (res)
