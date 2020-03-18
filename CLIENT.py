# MADE BY: Mar Danniel A. Ginturo
# DESKTOP CLIENT

import socket
import msvcrt


# Socket Connection

clie = socket.socket()
clie.connect(('-PUT-SERVER-IP-HERE-', 8000))
print("CLIENT : Connected to: ",clie.getsockname())

# Socket Sender

def keyPressFeed():
    keyPress = msvcrt.kbhit()
    if keyPress:
        keyPressBin = msvcrt.getch()
    else:
        keyPressBin = False
    return keyPressBin 

def clientRun(connection):
    while True:
        keyFeed = keyPressFeed()
        if keyFeed != False:
            connection.send(keyFeed)
            if keyFeed.hex() == "1b":
                connection.close()
                print("CLIENT KEY >: ", keyFeed, "Esc")
                print("CLIENT : Connection Terminated!")
                break
            print("CLIENT KEY >: ", keyFeed)


clientRun(clie)

