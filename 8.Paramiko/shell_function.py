import paramiko
import time

class ssh:
    def __init__(self,ip,usr,pwd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port=22,username=usr,password=pwd)
        self.shell = shell
        shell = ssh.invoke_shell()
        #return shell

    def sendxcmd(cmd):
        self.shell.send(cmd + "\n")
        while not self.shell.recv_ready():
            time.sleep(0.5)
        output = self.shell.recv(9999)
        return output.decode("utf-8")

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect("192.168.56.101",port=22,username='bacharya',password='iDirect')
# shell = ssh.invoke_shell()

ip = input("Enter the server ip:\n")
usr = input("Enter User Nmae:\n")
pwd = input("Enter the password:\n")

c=ssh(self,ip,usr.pwd)
#c.sshlogin(ip,usr,pwd)
log = open("C:\\python_test\\abc.txt","w")
log.write(c.sendxcmd("sudo bash"))
log.write(c.sendxcmd("iDirect"))
log.write(c.sendxcmd("cd /root/"))
log.write(c.sendxcmd("ls -ltr"))
log.write(c.sendxcmd("mkdir -p /tmp/test"))
log.write(c.sendxcmd("cd /tmp/test/"))
log.write(c.sendxcmd("cd .. "))
log.write(c.sendxcmd("pwd"))
# shell.send("rm -rf test\n")


