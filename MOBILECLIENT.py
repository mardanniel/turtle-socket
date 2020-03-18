# MADE BY: Mar Danniel A. Ginturo
# MOBILE CLIENT
# App used: Pydroid 3

import socket

# Socket Connection

clie = socket.socket()
clie.connect(('192.168.100.13', 8000))
print("CLIENT: Connected to: ",clie.getsockname())

# Socket Sender

def clientRun(connection):
    while True:
        try:
            clieMsg = input("SERVER: ")
            connection.send(clieMsg.encode())
            print("SERVER: ",clieMsg)
            if clieMsg.encode().hex() == "1b":
                connection.close()
                print("CLIENT: Connection Terminated!")
                break
        except UnicodeDecodeError:
            pass             
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