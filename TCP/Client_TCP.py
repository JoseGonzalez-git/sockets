#Importa las librerias del sockets
from socket import *
#Se define la dirección ip a donde se va a apuntar al servidor
servername ="localhost"
#Se define el puerto por donde escucha el servidor
serverport=12444
#Se establece la instancia del cliente sockets
clienteSocket= socket(AF_INET,SOCK_STREAM)
#Se establece la conexión con el servidor
clienteSocket.connect((servername,serverport))
#Se solicita al cliente que escriba un mensaje
msg=input("Escriba un número ")
#Se envia el mensaje al servidor con formato utf-8
clienteSocket.send(msg.encode('utf-8'))
#Se obtiene mensaje cambiado por el servidor
msg_modified=clienteSocket.recv(1024)
#se imprime el mensaje modificado por el servidor
print(msg, msg_modified, " es primo")
#Se cierra la conexion
clienteSocket.close()