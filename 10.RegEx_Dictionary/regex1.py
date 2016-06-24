import paramiko
import time
'''
This Function if for introducing delay until we get the output against a command sent to shell.
'''
def sendxcmd(shell,cmd):
    shell.send(cmd + "\n")
    while not shell.recv_ready():
        time.sleep(0.5)
    output = shell.recv(9999)
    return output.decode("utf-8")

dict = {'name': '', 'numfile': ''}
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.56.101",port=22,username='bak',password='iDirect')
shell = ssh.invoke_shell()
# log = open("C:\\python_test\\abc.txt","w")
sendxcmd(shell,"cd /tmp/test")
# log.write(sendxcmd(shell,"ll -ltr"))

# file1 = open("C:\\python_test\\abc.txt","r")

dict['name'] = sendxcmd(shell,"ls -l | awk \'{print $1}\'")
dict['numfile'] = sendxcmd(shell,"ls -l | awk \'{print $2}\'")

print(dict['name'])
print(dict['numfile'])

# shell.close()
# log.close()