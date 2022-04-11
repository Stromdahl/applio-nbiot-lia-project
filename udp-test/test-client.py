

import socket

 

msgFromClient       = "UDP test"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("46.101.231.12", 1790)

bufferSize          = 1024

 
print(f"sending: {msgFromClient}")

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

print("Sent")
