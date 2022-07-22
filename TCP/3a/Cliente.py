from socket import socket, AF_INET, SOCK_STREAM

def main():
    server_name = "localhost"
    server_port = 12444
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    exit = False
    option = 0
    while not exit:
        print ("1. Ingresar Estudiante")
        print ("2. Salir")
        print ("Elige una opcion")
        option = request_option()
        if option == 1:
            comunication_to_client(client_socket)
            message = client_socket.recv(1024)
            print(message.decode())
        elif option == 2:
            client_socket.send("Fin".encode())
            msg = client_socket.recv(1024)
            print(msg.decode())
            client_socket.close()
            exit = True

def request_option():
    correct = False
    num = 0
    while not correct:
        try:
            num = int(input("Ingrese un numero: "))
            correct = True
        except ValueError:
            print("El numero ingresado no es valido")
    return num

def comunication_to_client(client_socket):
    listnotes = []
    aux = 0
    identifications = int(input("Ingrese el ID del estudante: "))
    names = input("Ingrese los nombres del estudante: ")
    last_names = input("Ingrese los apellidos del estudante: ")
    while aux < 3:
        notes = input("Ingrese la nota {} y su porcentaje: ".format(aux + 1))
        listnotes.append(notes.split(","))
        aux += 1
    client_data = dict(id=identifications, name=names, last_name=last_names, note1=listnotes[0][0], note2=listnotes[1][
                       0], note3=listnotes[2][0], percentage1=listnotes[0][1], percentage2=listnotes[1][1], percentage3=listnotes[2][1])
    client_socket.send(str(client_data).encode())

if __name__ == "__main__":
    main()