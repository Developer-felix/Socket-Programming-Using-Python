import socket

s = socket.socket()

print("Socket Created")

s.bind(("localhost",9999))

s.listen(3)

print("Waiting for conections")

while True:
    c, addr = s.accept()

    print("Connected with",addr)

    c.send(bytes("Welcome to codewithfelix","utf-8"))

    c.close()
