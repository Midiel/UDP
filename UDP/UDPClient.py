#UDPClient.py

#timeout import needed to catch timeout exception
from socket import socket, SOCK_DGRAM, AF_INET, timeout

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# set timeout settings to 1.0 seconds
clientSocket.settimeout(1.0)

message = raw_input('Input lowercase sentence: ')
clientSocket.sendto(message, (serverName, serverPort))

try:
    modifiedMessage, addr = clientSocket.recvfrom(2048)
    print (modifiedMessage, addr)

# catch if timeout occurred
except timeout as e:
    print (e)
     
clientSocket.close()

#Allow the client to give up if no response has been reveived within 1 second.