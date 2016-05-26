import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("172.17.240.11",port=22,username='idirect',password='iDirect')
shell = ssh.invoke_shell()
# shell.send("su - \n")
# shell.send("iDirect\n")
shell.send("cd /tmp/ \n")
#time.sleep(1)
shell.send("ls -ltr \n")
time.sleep(1)
while not shell.recv_ready():
    time.sleep(2)
results = ''
while shell.recv_ready():
    results = results + shell.recv(1).decode("utf-8")
# shell.send("su -n")
# shell.send("su -n")
print(results)
