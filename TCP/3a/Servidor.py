from socket import socket, AF_INET, SOCK_STREAM
import ast
from operator import itemgetter


def main():
    server_port = 12444
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen()
    print("El servidor está listo para recibir peticiones: ")
    con_socket, addr = server_socket.accept()

    db = []
    while con_socket:
        print("Recibiendo mensajes desde el cliente", addr)
        data = con_socket.recv(1024)
        if not data.decode().__contains__("Fin"):
            db.append(data.decode())
            mensaje = "Dato guardado correctamente"
            con_socket.sendall(str(mensaje).encode())
        else:
            listdb = convert_dictionary(db)
            con_socket.sendall(str(order_db(new_list(listdb))).encode())
            con_socket.close()
            print("El servidor se ha cerrado")
            break

def new_list(listdb):
    newlist = []
    for i in range(len(listdb)):
        data = dict(id=listdb[i]['id'], name=listdb[i]['name'], last_name=listdb[i]['last_name'], note=(
            (float(listdb[i]['note1'])*int(listdb[i]['percentage1'])) + (float(listdb[i]['note2'])*int(listdb[i]['percentage2'])) + (float(listdb[i]['note3'])*int(listdb[i]['percentage3'])))/100)
        newlist.append(data)
    return newlist

def convert_dictionary(vector):
    for i in range(len(vector)):
        vector[i] = ast.literal_eval(vector[i])
    return vector

def order_db(db):
    newlist = sorted(db, key=itemgetter('last_name'))
    return newlist

if __name__ == "__main__":
    main()