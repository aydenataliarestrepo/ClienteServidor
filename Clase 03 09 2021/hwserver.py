#Provee la comunicación 
import zmq 

#Utilizo una caja para crear el socket
context = zmq.Context()

#Creo un socket al ser servidor utilizo zmq.REP 
s=context.socket(zmq.REP)

#Ligamos el socket a un puerto específico de sistema operativo en el 
#cual estoy corriendo como servidor 

s.bind('tcp://*:8001')

#Creo una variable (contador) e inicializo en cero
i=0 

# Para mantener el servidos atendiendo solicitudes creo un ciclo 
while True:
    print("Esperando solicitud {}".format(i))    #Para revisar el consumo de recursos del sistema
    i = i +1                        #Aumento el contador del ciclo 
    m = s.recv_string()             #El servidor inicia recibiendo una cadena
    print(m)                        #Imprimo el mensaje 
    s.send_string("mundo")          #Respondemos el mensaje
