from socket import *
from championship import *

port = 1881
server = socket(AF_INET, SOCK_STREAM)
server.bind(("", port))
server.listen(1)

print("Server waiting for connections")

while 1:
    conn, addr = server.accept()
    print("Receiving messages from client", addr)
    req = conn.recv(1024)
    teams = str(req).split(",")
    teams = list(map(lambda t : Team(t.strip()), teams))
    champion = Championship(teams)
    conn.send(str(champion).encode("utf-8"))
