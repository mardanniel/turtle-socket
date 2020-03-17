# MADE BY: Mar Danniel A. Ginturo

import socket
import msvcrt

# Socket Connection

clie = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clie.connect(('127.0.0.1', 50000))
print("CLIENT: Connected to: ",clie.getsockname())

# Socket Sender

def clientRun(connection):
    while True:
        try:
            clieMsg = msvcrt.getch()
            connection.send(clieMsg)
            print("SERVER: ",clieMsg.decode("utf-8"))
            if clieMsg.hex() == "1b":
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