import socket
from tkinter import E

def main():
    # Nombre del servidor
    server_name = "localhost"
    # server_port corresponde al puerto por donde escucha el servidor
    server_port = 12000
    # Se instancia un cliente socket de tipo UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Extrae del teclado una palabra escrita por el cliente
    print("A continuacion complete los sgtes datos: ")
    # Se ejecuta el comunicador
    comunication_to_client(client_socket, server_name, server_port)

def comunication_to_client(client_socket, server_name, server_port):
    while True:
        identification = int(input("Ingrese el ID del cliente: "))
        name = input("Ingrese el nombre del cliente: ")
        salary = float(input("Ingrese el salario del cliente: "))
        # Se crea una tupla con los datos del cliente
        client_data: str = '{},{},{}'.format(identification, name, salary)
        # Se envia la tupla al servidor
        client_socket.sendto(str(client_data).encode(),
                            (server_name, server_port))
        # Se recibe la respuesta del servidor
        message, server_address = client_socket.recvfrom(2048)
        # Se imprime la respuesta del servidor
        print("El servidor respondio: " + message.decode())
        print("\nDesde: ", server_address)
        # Se pregunta al cliente si desea ingresar otro cliente
        validator_client = client_contunue(client_socket, server_name, server_port)
        if validator_client == False:
            # Se recibe la respuesta del servidor
            message, server_address = client_socket.recvfrom(2048)
            print("Informacion almacenada en el servidor: ")
            print(message.decode())
            # Se cierra el socket
            client_socket.close()
            print("El cliente se ha cerrado")
            exit()

def client_contunue(client_socket, server_name, server_port):
    client_continue = input("Desea ingresar otro cliente? (s/n): ")
    if client_continue.upper() == "N":
        client_socket.sendto('Fin'.encode(), (server_name, server_port))
        return False
    elif client_continue.upper() != "S" and client_continue.upper() != "N":
        print("Ingrese una opcion valida")
        client_contunue(client_socket, server_name, server_port)
    else:
        return True


main()