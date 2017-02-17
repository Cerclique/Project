# -*- encoding:Utf-8 -*-

#-----------------------------------------------------------------------------#
#   Author : VERNIZEAU Aurélien                                               #
#   File : server.py                                                          #
#                                                                             #
#   Purpose : Wait for incomming message from client.py and return the        #
#             uppercase message                                               #
#-----------------------------------------------------------------------------#

# Different modules needed to do the projetct
from socket import *

# Creating server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Initialise server adress
server_adress = ("localhost", 12000)

# Bind the socket to the port
serverSocket.bind(server_adress)

while True:

    # Wait for incomming message, store data and adress
    data, adress = serverSocket.recvfrom(4096)

    # Answer with the uppercased data
    serverSocket.sendto(data.upper(), adress)
