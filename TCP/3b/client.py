from socket import *

port = 1881

client = socket(AF_INET, SOCK_STREAM)

client.connect(("localhost", port))

msg = input("Write the name of the teams separated by comma (min. 10, max. 20)\n")

client.send(msg.encode("utf-8"))

res = client.recv(2048)

print(res.decode("utf-8"))

client.close()
