#Provee la comunicación 
import zmq 

#Utilizo una caja para crear el socket
context = zmq.Context()

#Creo un socket al ser servidor utilizo zmq.REP 
s=context.socket(zmq.REP)

#Ligamos el socket a un puerto específico de sistema operativo en el 
#cual estoy corriendo como servidor 

s.bind('tcp://*:8001')

# Para mantener el servidos atendiendo solicitudes creo un ciclo 
while True:
    print("¡Esperando operación!")  #Mensaje o banner del servidor 
    p= s.recv_string()             #El servidor inicia recibiendo una cadena
    print(p)                        #Imprimo el mensaje 
    try:
        rta=str(eval(p))
        print("Ingresa")
    except:
        rta="Operacion no válida"
    s.send_string("Respuesta:" + rta) #Enviamos solución 
