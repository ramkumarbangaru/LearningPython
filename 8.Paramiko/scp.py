import paramiko
import time

def sendxcmd(shell,cmd,expectstring = "", waittime = 10):
    shell.send(cmd + "\n")

    while not shell.recv_ready():
        time.sleep(0.5)

    output = shell.recv(9999)
    waititeration = 1
    if expectstring != "":
        while expectstring not in output.decode("utf-8") and waititeration < waittime * 60:
            if shell.recv_ready():
                output = output + shell.recv(9999)
            time.sleep(1)
            waititeration = waititeration + 1
    return output.decode("utf-8")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("172.17.225.10",port=22,username='idirect',password='iDirect')
shell = ssh.invoke_shell()

log = open("C:\\python_test\\abc.txt","w")
log.write(sendxcmd(shell,"su -"))
log.write(sendxcmd(shell,"iDirect"))
log.write(sendxcmd(shell,"ls -ltr"))
log.write(sendxcmd(shell,'/usr/pgsql-9.1/bin/pg_dump -Fc configuration > /var/idirect/cache/config.dump; ll','total'))
log.write(sendxcmd(shell,"ls -ltr"))
# shell.send("rm -rf test\n")
