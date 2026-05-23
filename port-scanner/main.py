import socket

target = input("Enter target IP or website: ")

port = int(input("Enter port: "))

s = socket.socket()

s.settimeout(3)

result = s.connect_ex((target, port))

if result == 0:
    print("Port", port, "is OPEN")

else:
    print("Port", port, "is CLOSED")

s.close()
