import socket

BUFSIZE = 1000000
ip_port = ("", 1883)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ip_port)
head = 0
end = 0
tmp1 = []
while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    for i in data:
        if i == ';':
            print("hhh")
        elif i == 'p':
            print("y_predict")
        else:
            print("alal")
    server.sendto(data.upper(), client_addr)
server.close()
