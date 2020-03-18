# MADE BY: Mar Danniel A. Ginturo
# MOBILE CLIENT
# App used: Pydroid 3

import socket

# Socket Connection

clie = socket.socket()
clie.connect(('-PUT-SERVER-IP-HERE-', 8000))
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
