from socket import socket, AF_INET, SOCK_STREAM

def main():
    server_port = 12444
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen()
    print("El servidor está listo para recibir peticiones: ")
    con_socket, addr = server_socket.accept()
    print("El servidor esta listo para recibir datos")
    comunication(con_socket,addr)

def comunication(con_socket,addr):
    db =[]
    while con_socket:
        print("Recibiendo mensajes desde el cliente", addr)
        data = con_socket.recv(1024)
        print("El cliente envio: ")
        if  data.decode() == '1':
            print("Ordenando por apellido")
            order_db_by_surname(db)
            message = '{}'.format(db)
            con_socket.sendall(message.encode())
        elif data.decode() == '2':
            print("Filtrando por tamaño perfecto")
            con_socket.sendall(str(filter_db_by_perfect_size(db)).encode())
        elif data.decode() == '3':
            print("Filtrando por color de ojos")
            con_socket.sendall(str(filter_db_by_eye_color(db)).encode())
        elif data.decode() == '4':
            print("Ordenando por altura descendente")
            order_db_by_height_desc(db)
            message = '{}'.format(db)
            con_socket.sendall(message.encode())
        elif data.decode()== '5':
            message = "El servidor se ha cerrado"
            print(message)
            con_socket.sendall(message.encode())
            con_socket.close()
            break
        else:
            for i in data.decode():
                print(i, end="")
            append_db(data.decode().split(","),db)
            print("\nLa base de datos actual es: ", db)
            message = "El servidor recibio el dato correctamente."
            con_socket.sendall(message.encode())

def order_db_by_surname(db):
    db.sort(key=lambda x: x[0])

def filter_db_by_perfect_size(db):
    arr_perfect_size = []
    for i in db:
        if int(i[5]) == 90 and int(i[6]) == 60 and int(i[5]) == int(i[7]):
            arr_perfect_size.append(i)
    return arr_perfect_size

def filter_db_by_eye_color(db):
    arr_eye_color = []
    for i in db:
        if str(i[4]).upper() == "AZUL":
            arr_eye_color.append(i)
    return arr_eye_color

def order_db_by_height_desc(db):
    db.sort(key=lambda x: x[3], reverse=True)

def append_db(data,db):
    db.append([data[0], data[1], int(data[2]), float(data[3]), data[4], float(data[5]), float(data[6]), float(data[7])])



if __name__ == "__main__" :
    main()