#Provee la comunicación 
import zmq 

#Utilizo una caja para crear el socket
context = zmq.Context()

#Creo un socket 
s=context.socket(zmq.REQ)

#Conecto el socekt con el equipo local en el puerto  8001 
s.connect('tcp://localhost:8001')

#Envio el mensaje al servidor 
s.send_string("Hola")

#Almaceno la respuesta del servidor 
m=s.recv_string()

#Imprimo el mensaje recibido 
print(m)
