 
#/usr/bin/python

import socket
import sys

try: # esta estructura permite capturar comportamientos anomalos
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # COMPLETE (1)
except socket.error, msg: # si es del tipo socket.error
	print "Failed to create socket. Error code: " + str(msg[0]) + ", error message: " + msg[1] 
	sys.exit()

print "Socket created"

host = "localhost"
# defina una variable port y almacene alli el numero 80
port = 8080 # COMPLETE (2)


try:
	remote_ip = socket.gethostbyname(host) # COMPLETE (3)
except socket.gaierror:
	print "Hostname could not be resolved. Exiting"
	sys.exit()

# COMPLETE (4)
print ("IP address of " + host + " is " + remote_ip ) 

# COMPLETE (5)
endpoint = (remote_ip, port)

# COMPLETE (6)
s.connect(endpoint)

print "Socket connected to " + host + " on ip " + remote_ip

# Datos a enviarse
message = "GET / HTTP/1.1\r\nHost: " + host + "\r\n\r\n"

try:
	# COMPLETE (7)
    s.sendall(message)
except socket.error:
	print "Send failed"
	sys.exit()

print "Message send successfullly"

# Recibiendo datos
# COMPLETE (8)
reply = s.recv(1024)
print reply
s.close()