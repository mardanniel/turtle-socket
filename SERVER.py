# MADE BY: Mar Danniel A. Ginturo

import socket
import turtle

# Socket Receiver

def serverRun(connection, screen):
    while True:
        clientMsg = connection.recv(1024)
        print("CLIENT: ",clientMsg.hex())
        
        if clientMsg.hex() == "77": 
            tforward()
        elif clientMsg.hex() == "73":
            tbackward()
        elif clientMsg.hex() == "61":
            tleft()
        elif clientMsg.hex() == "64":
            tright()
        elif clientMsg.hex() == "48":
            tincrease()
        elif clientMsg.hex() == "50":
            tdecrease()
        elif clientMsg.hex() == "4b":
            tcolorLeft()
        elif clientMsg.hex() == "4d":
            tcolorRight()
        elif clientMsg.hex() == "1b":
            texit()
            break
        screen.update()

# Socket Connection

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servHost = '127.0.0.1'
servPort = 50000
serv.bind((servHost, servPort))
serv.listen()
print("SERVER: Server Established")
connA, connB = serv.accept()
print("SERVER: Connection to",connB,"successful!")

# Turtle Instantiation

w = 1
l = 1
colors = ["blue", "yellow", "orange","black", "red", "purple", "green"]
defcolor = 3

servScreen = turtle.Screen()
servScreen.setup(width=1024, height=768, startx=None, starty=None)
servTurtle = turtle.Turtle()
servTurtle.shape('turtle')

# Key Functions

def tforward():
    servTurtle.forward(20)
def tbackward():
    servTurtle.backward(20)
def tleft():
    servTurtle.left(90)
def tright():
    servTurtle.right(90)
def tincrease():
    global w,l
    w = w + 1
    l = l + 1
    servTurtle.resizemode("user")
    servTurtle.turtlesize(w,l,1)
def tdecrease():
    try:
        global w,l
        if w - 1 == 0 and l - 1 == 0: # Prevents from decreasing the size to 0
            w = 1
            l = 1
        else:
            w = w - 1
            l = l - 1
        servTurtle.resizemode("user")
        servTurtle.turtlesize(w,l,1)
    except turtle.TurtleGraphicsError:
        pass
def tcolorLeft():
    try:
        global colors, defcolor
        if defcolor - 1 == -1:
            defcolor = 0
        else:
            defcolor = defcolor - 1
            servTurtle.color(str(colors[defcolor]))
    except:
        pass
def tcolorRight():
    try:
        global colors, defcolor
        if defcolor + 1 == len(colors):
            defcolor = 6
        else:
            defcolor = defcolor + 1
            servTurtle.color(str(colors[defcolor]))
    except:
        pass
def texit():
    global serv, connA
    print("SERVER: Program and Connection Terminated! ")
    servScreen.bye()
    serv.close()
    connA.close()

serverRun(connA, servScreen)




