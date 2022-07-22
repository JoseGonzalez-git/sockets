from socket import socket, AF_INET, SOCK_STREAM

server_port = 12444
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print("El servidor está listo para recibir peticiones: ")

db = []
while 1:
    con_socket, addr = server_socket.accept()
    print("Recibiendo mensajes desde el cliente", addr)
    data = con_socket.recv(1024)
    if not data.decode().__contains__("Fin"):
        db.append(data.decode())
        mensaje = "Dato guardado correctamente"
        con_socket.send(str(mensaje).encode())
    else:
        print("La base de datos actual es: ", db)
        con_socket.send(str(db).encode())
        con_socket.close()
        print("El servidor se ha cerrado")
        break

    #print("Mensaje recibido: ", msg.decode())