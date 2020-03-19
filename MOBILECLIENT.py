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
            #To send w,a,s,d character keys to SERVER, just type
            #w for forward
            #a for left
            #s for backward
            #d for right
            #Ex. SERVER: w
            #NOTE: Capital character keys doesnt qualify
            #To send special keys to SERVER, just type
            #UP for 
            #DOWN for backward
            #LEFT for left
            #RIGHT for right
            #ESC for escape
            #Ex. SERVER: UP
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
