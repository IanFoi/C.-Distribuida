import simpy
import time
from Nodo import *
from Canales.CanalBroadcast import *

# La unidad de tiempo
TICK = 1


class NodoBroadcast(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de Broadcast.'''

    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida, mensaje=None):
	#Tu codigo aqui
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.mensaje = mensaje
        self.seen_message =  False

    def broadcast(self, env):
        ''' Algoritmo de Broadcast. Desde el nodo distinguido (0)
            vamos a enviar un mensaje a todos los demás nodos.'''
        # Tú código aquí
        if self.id_nodo == 0 :
            print("Nodo 0 inicializando")
            yield env.timeout(TICK)
            #self.mensaje = "OK"
            self.seen_message = True 
            self.canal_salida.envia(self.mensaje,self.vecinos)
        else:
            self.mensaje = None
            print("NODO",self.id_nodo)
            print("mensaje: ",self.mensaje)


        while True :
            if self.seen_message == False :
                self.seen_message = True  
                self.mensaje = yield self.canal_entrada.get()
                self.canal_salida.envia(self.mensaje,self.vecinos)
                print("Nodo: ",self.id_nodo)
                print("Mensaje recibido: ",self.mensaje)
                
            else:
                break

    
adyacencias = [[1, 2], [0, 3], [0, 3, 5], [1, 2, 4], [3, 5], [2, 4]]


env  = simpy.Environment()
canal = CanalBroadcast(env)
grafica = []

for i in range(0,len(adyacencias)): # 0,n-1
    grafica.append( NodoBroadcast(i,adyacencias[i],canal.crea_canal_de_entrada(),canal,"HOLA"))


for nodo in grafica :
    env.process(nodo.broadcast(env))


env.run(until = 15)




