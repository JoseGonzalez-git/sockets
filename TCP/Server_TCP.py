#Se importan todas las librerias de sockets
from socket import *
#puerto por donde escuchará el servidor
#La función numero_primo, permite determinar si un número es primo o no.
#
def numero_primo(numero):
    i=2
    es_primo=True
    while ((i<numero) and (es_primo)):
        if numero % i == 0:
            es_primo=False
        else :
            i=i+1
    return es_primo

serverPort =12444
#Se instancia el servidor TCP
serverSocket = socket(AF_INET,SOCK_STREAM)
#Se define el puerto del servidor
serverSocket.bind(('',serverPort))
#Servidor en modo escucha
serverSocket.listen(1)
print("El servidor está listo para recibir peticiones: ")
while 1:
    #Se extrae la información del puerto y la dirección ip del servidor
    conSocket, addr = serverSocket.accept()
    print("Recibiendo mensajes desde el cliente", addr)
    #Obtiene la información extraida del cliente
    msg= conSocket.recv(1024)
    n= int(msg)
    new_msg="NO";
    if numero_primo(n) is True:
        new_msg ="SI";
    conSocket.send(new_msg.encode('utf-8'))
