import socket

#Creating Socket
#IPV6,TCP
s=socket.socket()
print("Socket Created")
#Bind with port
s.bind(("localhost",9999))

s.listen()
print("Waiting For Connection")

while True:
    c,addr=s.accept()
    name = c.recv(1024).decode()
    print("Connected With",addr,name)
    c.send(bytes("Welcome to Zakirdev","utf-8"))
    c.close()
