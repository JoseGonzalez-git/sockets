import socket
# Nombre del servidor
serverName = "localhost"
# ServerPort corresponde al puerto por donde escucha el servidor
serverPort = 12000
# Se instancia un cliente socket de tipo UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Extrae del teclado una palabra escrita por el cliente
initial_sms = print("A continuacion complete los sgtes datos: ")
validator_client = True
while validator_client:
    id = int(input("Ingrese el ID del cliente: "))
    name = input("Ingrese el nombre del cliente: ")
    salary = float(input("Ingrese el salario del cliente: "))
    # Se crea una tupla con los datos del cliente
    client_data:str = '{}, {}, {}'.format(id, name, salary)
    # Se envia la tupla al servidor
    client_socket.sendto(str(client_data).encode(), (serverName, serverPort))
    # Se recibe la respuesta del servidor
    message, serverAddress = client_socket.recvfrom(2048)
    # Se imprime la respuesta del servidor
    print("El servidor respondio: " + message.decode())
    # Se pregunta al cliente si desea ingresar otro cliente
    clientContinue = input("Desea ingresar otro cliente? (s/n): ")
    if clientContinue.upper() == "N":
        validator_client = False
    elif clientContinue.upper() != "S" and clientContinue.upper() != "N":
        print("Ingrese una opcion valida")
        clientContinue = input("Desea ingresar otro cliente? (s/n): ")
    else:
        validator_client = True
# Se cierra el socket
client_socket.close()
print("El cliente se ha cerrado")
# Se termina el programa
exit()
