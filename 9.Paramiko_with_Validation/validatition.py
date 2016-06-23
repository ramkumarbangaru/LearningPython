import paramiko
import time


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
# log.write(sendxcmd(shell,"ll"))
log.write(sendxcmd(shell,"/bin/ls -ls | awk \'{print $10}\'"))
shell.close()
log.close()


file1 = open("C:\\python_test\\abc.txt","r")
#list1 = file1.read()

# list2 = list1.decode("utf-8")

#print(list1)

for word in (file1.read()):
    print (word)
   # if line == "temp.txt":
   #  print("TRUE")
   #  exit()
   # else:
   #  print("False")


# shell.send("rm -rf test\n")
