# -*- encoding:Utf-8 -*-

#-----------------------------------------------------------------------------#
#   Author : VERNIZEAU Aurélien                                               #
#   File : client.py                                                          #
#                                                                             #
#   Purpose : Send ping to the server using UDP_socket, wait for the          # 
#             answer/timeout and estimate the RTT                             #
#-----------------------------------------------------------------------------#

# Different modules needed to do the project
from socket import *
from datetime import datetime

# Creation of the socket that we will use to send message
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Initialise the message
message = "Ping"

# Initialise the counter
counter = 1

while counter < 11:

    # First time request to calculate the RTT of the message
    startingTime = datetime.now()

    # We send the message to the server
    clientSocket.sendto(message,('localhost', 12000))

    # Print out the sending message and the date
    print(message + " " + str(counter) + " " + str(startingTime))

    # Set the timeout of the socket at 1000ms
    clientSocket.settimeout(1)

    # Using the try...except method to easily print out response in different cases (message lost or not)
    try:
        # Reception of the modified message
        modifiedMessage, serverAdress = clientSocket.recvfrom(2048)

        # Second time request
        endingTime = datetime.now()

        # calculate the RTT of the message using the 2 time resquest
        time = endingTime - startingTime

        # Print out the modified message receive from the server and the RTT in microseconds
        print modifiedMessage + "\tRTT = " + str(time.microseconds) +"\n"

    except timeout:
        # Print out if the message get lost
        print "Request timed out\n"

    # Incrementation of the counter each time a message is sent
    counter += 1

print("Transmission finished -- Closing socket")
# Close client socket
clientSocket.close()
