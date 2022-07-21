from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("El servidor esta listo para recibir datos")
message = "El servidor recibio el dato correctamente."
db =[]
while 1:
    data, clientAddress = serverSocket.recvfrom(2048)
    print("El cliente envio: ")
    for i in data.decode():
        print(i, end="")
    print("\nDesde: ", clientAddress)
    db.append(data.decode().split(","))
    print("\nLa base de datos actual es: ", db)
    serverSocket.sendto(message.encode(), clientAddress)
