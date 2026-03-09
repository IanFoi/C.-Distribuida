import simpy
import time
from Nodo import *
from Canales.CanalBroadcast import *

# La unidad de tiempo
TICK = 1


class NodoTopologia(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de Broadcast.'''

    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida, mensaje=None):
	#Tú código aquí
        self.id_nodo = id_nodo
        self.vecinos = vecinos 
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.proc_conocidos= {id_nodo}
        self.canales_conocidos = set()
        # El nodo agrega a sus vecinos a su conjunto de conocidos como una tupla (Id, vecino).
        for vecino in self.vecinos:
            self.canales_conocidos.add(tuple(sorted([self.id_nodo, vecino])))    
        
    def topologia(self, env):
        # Tú código aquí
        for vecino_j in self.vecinos:
            self.canal_salida.envia((self.id_nodo, self.vecinos), vecino_j)

        while True:
            position_recibida = yield self.canal_entrada.get()
            k, vecinos_k = position_recibida
            if k not in self.proc_conocidos:
                self.proc_conocidos.add(k)
                for vecino in vecinos_k:
                    self.canales_conocidos.add(tuple(sorted([k, vecino])))
                
                for vecino in self.vecinos:
                    if vecino.id_nodo != k:
                        self.canal_salida.envia((k, vecinos_k), vecino)
                    else:
                        continue
                conceGrafica = True
                for (l,m) in self.canales_conocidos:
                    if l not in self.proc_conocidos or m not in self.proc_conocidos:
                        conceGrafica = False
                        return
