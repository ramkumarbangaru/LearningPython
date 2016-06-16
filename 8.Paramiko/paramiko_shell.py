import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.56.101",port=22,username='bak',password='iDirect')
shell = ssh.invoke_shell()
log = open("C:\\python_test\\abc.txt","w")

# shell.send("su - \n")
# shell.send("iDirect\n")
shell.send("cd /tmp/ \n")
output = ''
#time.sleep(1)
while not shell.recv_ready():
    time.sleep(2)
output = shell.recv(1024)
# if shell.recv_ready():
#     output = shell.recv(9999)
# print(output)
for ln in output.decode("utf-8").split('\n'):
    print (ln)
    log.writelines(ln)

shell.close()
ssh.close()
log.close()
# #time.sleep(1)
# shell.send("ls -ltr \n")
# time.sleep(1)
# while not shell.recv_ready():
#     time.sleep(2)
# results = ''
# while shell.recv_ready():
#     results = results + shell.recv(1).decode("utf-8")
# # shell.send("su -n")
# # shell.send("su -n")
# print(results)
# test
