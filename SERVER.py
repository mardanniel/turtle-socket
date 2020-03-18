# MADE BY: Mar Danniel A. Ginturo
# DESKTOP SERVER

import socket
import turtle

# Socket Receiver

def serverRun(connection, screen):
    while True:
        clientMsg = connection.recv(1024)
        print("SERVER FEED >: ",clientMsg.hex())
        if clientMsg.hex() == "77":     #W
            tforward()
        elif clientMsg.hex() == "73":   #S
            tbackward()
        elif clientMsg.hex() == "61":   #A
            tleft()
        elif clientMsg.hex() == "64":   #D
            tright()

        #   KEY PRESS ON DESKTOP     || SENDING COMMANDS ON MOBILE
        elif clientMsg.hex() == "48" or clientMsg.hex() == "5550":   #Up Arrow Key
            tincrease()
        elif clientMsg.hex() == "50" or clientMsg.hex() == "444f574e":   #Down Arrow Key
            tdecrease()
        elif clientMsg.hex() == "4b" or clientMsg.hex() == "4c454654":   #Left Arrow Key
            tcolorLeft()
        elif clientMsg.hex() == "4d" or clientMsg.hex() == "5249474854":   #Right Arrow Key
            tcolorRight()
        elif clientMsg.hex() == "1b" or clientMsg.hex() == "455343":   #Escape
            texit()
            break
        screen.update()

# Socket Connection

serv = socket.socket()
servHost = 'PUT-YOUR-IP-HERE'
servPort = 8000
serv.bind((servHost, servPort))
serv.listen()
print("SERVER: Server Established at",servHost)
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




