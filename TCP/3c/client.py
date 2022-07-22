from socket import socket, AF_INET, SOCK_STREAM

def main():
    server_name = "localhost"
    server_port = 12444
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    print("El servidor está listo para recibir peticiones: ")
    comunication_to_client(client_socket, server_name, server_port)

def comunication_to_client(client_socket, server_name, server_port):
    while True:
        name = input("Ingrese el nombre: ")
        surname = input("Ingrese el apellido: ")
        age = int(input("Ingrese la edad: "))
        height = float(input("Ingrese la altura: "))
        color_eyes = input("Ingrese el color de los ojos: ")
        bust_size = float(input("Ingresar la medida del Busto: "))
        waist_size = float(input("Ingresar la medida del Cintura: "))
        hip_size = float(input("Ingresar la medida del Cadera: "))
        # Se crea una tupla con los datos del cliente
        client_data: str = '{},{},{},{},{},{},{},{}'.format(surname, name, age,height,color_eyes,bust_size,waist_size,hip_size)
        # Se envia la tupla al servidor
        client_socket.send(client_data.encode())
        # Se recibe la respuesta del servidor
        message = client_socket.recv(2048)
        # Se imprime la respuesta del servidor
        print("El servidor respondio: " + message.decode())
        # Se pregunta al cliente si desea ingresar otro cliente
        validator_client = client_contunue(client_socket, server_name, server_port)
        if validator_client == False:
            menu(client_socket)
            break

def client_contunue(client_socket, server_name, server_port):
    client_continue = input("Desea ingresar otro cliente? (s/n): ")
    if client_continue.upper() == "N":
        return False
    elif client_continue.upper() != "S" and client_continue.upper() != "N":
        print("Ingrese una opcion valida")
        client_contunue(client_socket, server_name, server_port)
    else:
        return True

def menu(client_socket):
    while True:
        print("Sele ccione una opcion: (1,2,3,4,5)")
        print("1. Candidatas ordenadas por apellido.")
        print("2. Lista de candidatas con medidas perfectas.")
        print("3. Lista de candidatas con Ojo color azul.")
        print("4. Listado de candidatas con segun su estatura. Descendente.")
        print("5. Salir")
        option = int(input("Ingrese una opcion: "))
        client_socket.send(str(option).encode())
        if option == 5:
            print("Gracias por usar el servicio")
            client_socket.send('Fin'.encode())
            client_socket.close()
            break
        message = client_socket.recv(2048)
        # Se imprime la respuesta del servidor
        print("El servidor respondio: " + message.decode())


if __name__ == "__main__":
    main()