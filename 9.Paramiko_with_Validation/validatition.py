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

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.56.101",port=22,username='bak',password='iDirect')
shell = ssh.invoke_shell()
log = open("C:\\python_test\\abc.txt","w")
sendxcmd(shell,"cd /tmp")
log.write(sendxcmd(shell,"ll -ltr"))
# log.write(sendxcmd(shell,"/bin/ls -ls | awk \'{print $10}\'"))
shell.close()
log.close()

file1 = open("C:\\python_test\\abc.txt","r")
#print(file1)
if "temp.txt" in file1.read():  # in case we used onle file1 instead of file1.read(), its reading just the first line not whole file
    print("TRUE")
else:
    print("FALSE")



