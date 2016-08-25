import paramiko
import time
import re
import operator


'''
This Function if for introducing delay until we get the output against a command sent to shell.
'''
def sendxcmd(shell,cmd):
    shell.send(cmd + "\n")
    while not shell.recv_ready():
        time.sleep(0.5)
    output = shell.recv(9999)
    return output.decode("utf-8")

dict1 = {'name': '', 'date': ''}
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.56.101",port=22,username='bak',password='iDirect')
shell = ssh.invoke_shell()
# log = open("C:\\python_test\\abc.txt","w")
# sendxcmd(shell,"mkdir -p /tmp/test")
# sendxcmd(shell,"mkdir -p /tmp/test/file1")
# sendxcmd(shell,"mkdir -p /tmp/test/file2")
sendxcmd(shell,"cd /tmp/test")
# log.write(sendxcmd(shell,"ll -ltr"))
s= sendxcmd(shell,"ls -ltr")
print("The below is the op for ls -ltr cmd:")
print(s)
name = re.findall(r'\w+\.txt',s,re.M)
print(name)
# dict1['name']=name.group()

date = re.findall(r'\w{3} \d{2} \d{2}:\d{2}',s,re.M)
print(date)
# dict1['date']=date.group()

# print(dict1)

dict2 = dict(zip(name,date))
print(dict2)

print("===============================")
print(sorted(dict2.keys()))
print(sorted(dict2.values()))
print("===============================")
print(sorted(dict2.keys(),reverse=True))
print(sorted(dict2.values(),reverse=True))
print("+++++++++++++++++++++++++++++++")
for v in sorted( dict2.values(),reverse=True):
    for key in dict2:
        if dict2[ key ] == v:
            print (key, v)
            break
print("+++++++++++++++++++++++++++++++")
for v in sorted( dict2.values()):
    for key in dict2:
        if dict2[ key ] == v:
            print (key, v)
            break
print("+++++++++++++++++++++++++++++++")
print(sorted(dict2.items(),reverse=True))

# file1 = open("C:\\python_test\\abc.txt","r")

# dict['name'] = sendxcmd(shell,"ls -l | awk \'{print $9}\'")
# # time.sleep(0.1)
# dict['numfile'] = sendxcmd(shell,"ls -l | awk \'{print $6 $7 $8}\'")

# print(dict['name'])
# print(dict['numfile'])

# shell.close()
# log.close()