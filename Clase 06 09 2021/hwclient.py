#Provee la comunicación 
import zmq 
import sys 

#Utilizo una caja para crear el socket
context = zmq.Context()

#Creo un socket 
s=context.socket(zmq.REQ)

#Conecto el socekt con el equipo local en el puerto  8001 
s.connect('tcp://localhost:8001')

#Variable que almacena el mensaje del cliente
p= sys.argv[1]

#Envio la operacion al servidor
s.send_string(str(p))

#Almaceno la respuesta del servidor 
m=s.recv_string()

#Imprimo el mensaje recibido 
print(m)
