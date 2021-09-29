#Provee la comunicación 
import zmq 

#Utilizo una caja para crear el socket
context = zmq.Context()

#Creo un socket al ser servidor utilizo zmq.REP 
s=context.socket(zmq.REP)

#Ligamos el socket a un puerto específico de sistema operativo en el 
#cual estoy corriendo como servidor 

s.bind('tcp://*:8001')

#El servidor inicia recibiendo una caden 
m = s.recv_string()

#Respondemos el mensaje
s.send_string("mundo")
