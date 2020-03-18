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

# =
# KEYS and HEX
# Esc   =62275c78316227 or 1b
# W     =62277727 or 77
# A     =62276127 or 61
# S     =62277327 or 73
# D     =62276427 or 64
# Up    =62274827 or e0-48
# Down  =62275027 or e0-50
# Left  =62274b27 or e0-4b
# Right =62274d27 or e0-4d
# =
