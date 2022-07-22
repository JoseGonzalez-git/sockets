import socket

def main():
    server_port = 12000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("", server_port))
    print("El servidor esta listo para recibir datos")
    comunication(server_socket)

def comunication(server_socket):
    db =[]
    while 1:
        data, client_address = server_socket.recvfrom(2048)
        print("El cliente envio: ")
        if not data.decode().__contains__("Fin"):
            for i in data.decode():
                print(i, end="")
            append_db(data.decode().split(","),db)
            print("\nDesde: ", client_address)
            print("\nLa base de datos actual es: ", db)
            message = "El servidor recibio el dato correctamente."
            server_socket.sendto(message.encode(), client_address)
        else:
            print(data.decode())
            order_db(db)
            message = ""
            for i in db:
                message += str(i[0]) + "," + i[1] + "," + str(i[2]) + "\n"
            print(message)
            server_socket.sendto(message.encode(), client_address)
            server_socket.close()
            print("El servidor se ha cerrado")
            break

def order_db(db):
    return db.sort(key=lambda x: x[0])

def append_db(data,db):
    db.append([int(data[0]), data[1], float(data[2])])

if __name__ == "__main__" :
    main()