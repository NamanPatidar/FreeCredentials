#Establishing connection over using socket mySocket.. host is data.pr4e.org over port 80
import socket
mySocket = socket.socket(socket.AF_INET, socket.sock_STREAM)
mySocket.connect(('data.pr4e.org', 80)) 
