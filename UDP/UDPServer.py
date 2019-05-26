#UDPServer.py

# To generate random number for the lost package part, and to calculate time
import random, time


#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.
from socket import socket, SOCK_DGRAM, AF_INET

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print "Waiting for connections"
while True:
    # Start the clock
    start = time.time()

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2048)
    # Capitalize the message from the client
    print message, address
    message = message.upper()

    #Configure the server so that it randomly drops packets.
    # Generate random number between 0 to 10
    rand = random.randint(0, 10)
    if rand < 3:
        print("Ops!! Lost that packet.")
    else:
        serverSocket.sendto(message, address)

    #Include information about how long each response took. This will be the RTT.
    print("Response time (RTT): ", time.time()-start)

serverSocket.close() 


#Configure the server so that it randomly drops packets.
#Include information about how long each response took. This will be the RTT.