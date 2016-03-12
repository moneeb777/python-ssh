# python-ssh

The code is a practical implementation of the ssh server, ssh client and sftp over ssh in python.
Original tutorial is by infosec at: http://resources.infosecinstitute.com/creating-undetectable-custom-ssh-backdoor-python-z/

The server.py file creates as ssh server listening on port 22 with default creds root/toor. The client.py file attempts to connect
to this server. Once a connection is made, the server can execute commands on the client very similar to cmd. If the server gets an
'exit' commands, it cleanly shuts down both the server and client. 

SFTP is used to grab files from the client. The following command would send test.txt back to the server:
grab*test*C:\test\test.txt
